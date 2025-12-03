I am working on a technical guide comparing JSF (JavaServer Faces) to modern architectures like Next.js/RSC. I need to generate specific visuals to illustrate the concepts.

Please generate the following images using your `generate_image` tool. Save them to the `images/` directory (or let me know where you save them so I can move them).

**Context:**
The guide argues that web architecture is cyclical (Server -> Client -> Server) and that modern Server Components (RSC) are a return to the principles of JSF but with better technology.

**Images to Generate:**

1.  **`best_practices_comparison.png`**
    *   **Prompt:** Comparison Checklist: LEFT (JSF - Built-in): Shield icon (CSRF), Lock icon (Validation), Type icon (Types). All Green checks. RIGHT (SPA - Manual): Empty boxes or Red crosses for these, labeled 'Manual Implementation Required'. Title: 'Batteries Included vs DIY'.

2.  **`spiral_ascent_final.png`**
    *   **Prompt:** 3D Spiral moving upwards. Bottom loop: 'JSF (2006)'. Middle loop: 'SPA (2015)'. Top loop: 'RSC (2024)'. The top loop is directly above the bottom loop but higher up. Labels: 'Same Principles, Better Tech'. Title: 'The Architecture Spiral'.

3.  **`comparison_save_user.png`**
    *   **Prompt:** Split screen code comparison. LEFT (JSF): Simple XML form with `<h:commandButton action="#{userBean.save}" />`. RIGHT (React): Complex `handleSubmit` function with `e.preventDefault()`, `fetch()`, `JSON.stringify()`, and error handling. Title: 'The Cost of Control: Declarative vs Imperative'.

4.  **`comparison_datatable.png`**
    *   **Prompt:** Visual representation of a Data Table. LEFT (PrimeFaces): A rich table with sorting/filtering icons, labeled '1 Tag: <p:dataTable>'. RIGHT (React): A wireframe showing multiple components (Header, Row, Cell, Pagination) connected by wires, labeled 'Manual Composition'. Title: 'Component Abstraction'.

5.  **`comparison_ajax.png`**
    *   **Prompt:** AJAX Flow Diagram. LEFT (JSF): Button -> Server -> Partial Update (Green area). Simple loop. RIGHT (SPA): Button -> State Change -> API Call -> JSON Response -> State Update -> Re-render. Complex loop. Title: 'AJAX: Built-in vs Manual'.

6.  **`comparison_server_action.png`**
    *   **Prompt:** Server Action Diagram. LEFT (JSF): `#{bean.method()}` directly calling Java method. RIGHT (Next.js): `action={serverAction}` directly calling Node function. An equals sign (=) between them. Title: 'Server Actions: The Modern Managed Bean'.

**After generating these images, please let me know so I can integrate them into my markdown file.**