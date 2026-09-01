export type LearningStatus = "unseen" | "learning" | "review" | "mastered";
export interface QuestionLearningState { status: LearningStatus; favorite: boolean; lastVisitedAt?: string; }
export interface LearningState { questions: Record<string, QuestionLearningState>; }
export const LEARNING_STATE_KEY = "ai-llm-learning-library:v1";
export function getLearningState(): LearningState {
  try { const parsed = JSON.parse(localStorage.getItem(LEARNING_STATE_KEY) ?? "{}"); return { questions: parsed.questions && typeof parsed.questions === "object" ? parsed.questions : {} }; }
  catch { return { questions: {} }; }
}
export function updateQuestionState(id: string, patch: Partial<QuestionLearningState>): QuestionLearningState {
  const state = getLearningState(); const current = state.questions[id] ?? { status: "unseen", favorite: false }; state.questions[id] = { ...current, ...patch }; localStorage.setItem(LEARNING_STATE_KEY, JSON.stringify(state)); return state.questions[id];
}
export function clearLearningState() { localStorage.removeItem(LEARNING_STATE_KEY); }
