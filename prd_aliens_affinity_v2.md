# PRD: Alien Features Affinity Analysis
**Version**: 2.0

## Change Log
- **v2.0**: 
  - Added user-configurable dataset dimensions (rows, columns).
  - Implemented an iterative generation loop to guarantee at least one valid rule is found.
  - Made feature properties (names, probabilities) dynamic for custom feature counts.

## Project Overview
Create a synthetic dataset of alien records, then perform affinity analysis to discover meaningful relationships between feature combinations using Support, Confidence, and Lift metrics.

---

## 1. Dataset Generation Requirements

### 1.1 Dataset Structure
- **Format**: 2D NumPy array
- **Dimensions**: User-configurable. **Default: 5000 rows × 6 columns**.
- **Data Type**: Binary (0 or 1)

### 1.2 Feature Distribution Requirements
- For the default 6 features, a predefined descending probability distribution is used (70%, 60%, ..., 20%).
- For custom feature counts, probabilities are dynamically generated in a descending order to ensure an interesting mix of common and rare features.

### 1.3 **[NEW] Rule Guarantee Requirement**
- The script must ensure that the generated dataset yields **at least one** association rule that meets the filtering criteria (Support ≥ 30%, Confidence ≥ 70%).
- If a generated dataset produces no valid rules, it should be discarded, and a new dataset should be generated until the condition is met. The user should be notified of this process.

---

## 2. Affinity Analysis Requirements (Unchanged)

### 2.1 Metrics Definitions
- **Support**: `S = frq(X,Y) / N`
- **Confidence**: `C = frq(X,Y) / frq(X)`
- **Lift**: `Lift = P(Y|X) / P(Y)`

### 2.2 Filtering Criteria
- **Support ≥ 30%**
- **Confidence ≥ 70%**

---

## 3. Implementation Constraints (Unchanged)
- **Allowed**: NumPy only
- **Prohibited**: scikit-learn, mlxtend, or other pre-built libraries.

---

## 4. Output Requirements

### 4.1 **[UPDATED] User Interaction**
- On launch, the script will prompt the user to enter the desired number of records and features.
- Default values will be provided and used if the user simply presses Enter.
- The script will display status messages, including which attempt it is on during the dataset regeneration process.

### 4.2 Display Format
- The final output remains a clean, tabular format displaying the Rule, Support, Confidence, and Lift for all qualifying rules.

---

## 5. Success Criteria
- ✅ All previous criteria from v1.0.
- ✅ **[NEW]** Script successfully accepts user input for dimensions.
- ✅ **[NEW]** Script reliably finds and displays at least one valid rule, regardless of initial random data.
