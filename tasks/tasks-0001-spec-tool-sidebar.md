# Task List: Tool Sidebar Implementation

## Relevant Files

- `templates/navbar.html` - Add sidebar toggle button with inline SVG icon
- `templates/server/viewer.html` - Convert `.left-toolbar` to collapsible sidebar structure
- `templates/server/tools/_tool_wrapper.html` - Reusable foldout component wrapper (new file)
- `templates/server/tools/accessibility_analysis.html` - Accessibility analysis tool content (new file)
- `templates/server/tools/tool_2.html` - Placeholder tool 2 (new file)
- `templates/server/tools/tool_3.html` - Placeholder tool 3 (new file)
- `templates/server/tools/tool_4.html` - Placeholder tool 4 (new file)
- `templates/server/tools/tool_5.html` - Placeholder tool 5 (new file)
- `templates/server/tools/tool_6.html` - Placeholder tool 6 (new file)

### Notes

- This is a Django template-based project with no existing JavaScript files
- All JavaScript will be inline in `viewer.html` following existing pattern
- CSS will be inline in `viewer.html` `{% block extra_head %}` following existing pattern
- The project uses vanilla JavaScript (no frameworks)
- No test files are required as this is purely frontend template work
- Use Django's `{% include %}` tag for template composition
- All icons must be inline SVG (no external icon libraries)

## Tasks

- [x] 1.0 Implement Collapsible Sidebar with Single Static Foldout
  - Demo Criteria: "Navigate to /viewer/<pdf_id>/ and verify: (1) navbar has toggle button, (2) clicking toggle collapses sidebar to 40px width, (3) one foldout labeled 'Tool 1' is visible with placeholder content, (4) clicking foldout header expands/collapses content smoothly, (5) foldout content pushes subsequent content down when expanding"
  - Proof Artifact(s): "URL: http://localhost:8080/viewer/<pdf_id>/, Screenshot showing: sidebar collapsed (40px), sidebar expanded with foldout collapsed, sidebar expanded with foldout expanded"
  - [x] 1.1 Add sidebar toggle button to navbar with inline SVG icon
  - [x] 1.2 Update viewer.html CSS to support collapsible sidebar (350px expanded, 40px collapsed)
  - [x] 1.3 Create templates/server/tools/ directory structure
  - [x] 1.4 Create reusable _tool_wrapper.html foldout component with header and content sections
  - [x] 1.5 Create tool_1.html with placeholder content
  - [x] 1.6 Refactor viewer.html to use new sidebar structure with single foldout
  - [x] 1.7 Add JavaScript for sidebar toggle functionality
  - [x] 1.8 Add JavaScript for foldout expand/collapse functionality with smooth animations
  - [x] 1.9 Add CSS for foldout header hover states and chevron rotation
  - [x] 1.10 Add ARIA attributes for accessibility (aria-expanded, aria-controls, aria-labelledby)

- [ ] 2.0 Migrate Accessibility Analysis to Foldout Tool
  - Demo Criteria: "Navigate to /viewer/<pdf_id>/ with uploaded PDF containing accessibility data and verify: (1) first foldout is labeled 'Accessibility Analysis', (2) all existing data displays correctly (errors, warnings, summary stats, structure info, metadata), (3) styling matches original implementation, (4) default state is sidebar expanded with foldout collapsed"
  - Proof Artifact(s): "URL: http://localhost:8080/viewer/<pdf_id>/, Screenshot showing accessibility foldout expanded with real PDF data, Visual comparison with original implementation"
  - [ ] 2.1 Create accessibility_analysis.html template file
  - [ ] 2.2 Extract all accessibility content from viewer.html (lines 72-160) into accessibility_analysis.html
  - [ ] 2.3 Preserve all existing sections: errors, warnings, summary, document structure, metadata
  - [ ] 2.4 Maintain all existing styling and conditional logic
  - [ ] 2.5 Replace tool_1.html with accessibility_analysis.html in viewer.html using {% include %}
  - [ ] 2.6 Update foldout title from "Tool 1" to "Accessibility Analysis"
  - [ ] 2.7 Verify all extraction_result context variables are properly passed and displayed

- [ ] 3.0 Add Remaining Placeholder Tools and Finalize Composable Architecture
  - Demo Criteria: "Navigate to /viewer/<pdf_id>/ and verify: (1) sidebar contains 6 total foldouts (Accessibility Analysis + Tool 2-6), (2) multiple foldouts can be expanded simultaneously, (3) each tool has distinct header and placeholder content, (4) content grows unbounded without scrolling, (5) adding a new tool requires only creating a template file and one include line"
  - Proof Artifact(s): "URL: http://localhost:8080/viewer/<pdf_id>/, Screenshot showing multiple tools expanded, Code walkthrough demonstrating how to add 'Tool 7' in < 5 minutes"
  - [ ] 3.1 Create tool_2.html with placeholder content
  - [ ] 3.2 Create tool_3.html with placeholder content
  - [ ] 3.3 Create tool_4.html with placeholder content
  - [ ] 3.4 Create tool_5.html with placeholder content
  - [ ] 3.5 Create tool_6.html with placeholder content
  - [ ] 3.6 Add all 5 placeholder tools to viewer.html using {% include %} with _tool_wrapper.html
  - [ ] 3.7 Verify multiple foldouts can be expanded simultaneously
  - [ ] 3.8 Verify content grows unbounded without max-height constraints
  - [ ] 3.9 Test and document the process for adding a new tool (should take < 5 minutes)
