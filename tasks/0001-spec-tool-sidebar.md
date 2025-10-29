# Tool Sidebar Specification

## Introduction/Overview

The Tool Sidebar feature transforms the existing left toolbar in the PDF viewer into a composable, extensible tool panel system. Currently, the left toolbar displays only the accessibility analysis summary. This feature will reorganize it into a collapsible sidebar containing multiple expandable/collapsible foldout panels (tools), making it easy to add new tools in the future.

The sidebar will maintain its fixed position on the left side of the screen with a fixed width, and each tool will be independently expandable. This creates a scalable architecture for adding analysis tools, editing capabilities, and other features without cluttering the interface.

## Goals

1. Convert the existing `.left-toolbar` into a collapsible sidebar with a toggle mechanism in the navbar
2. Implement a foldout/accordion component system that allows multiple panels to be expanded simultaneously
3. Migrate the existing accessibility analysis content into the first foldout tool
4. Create a composable Django template architecture that makes adding new tools straightforward
5. Establish 6 total tool slots (1 accessibility summary + 5 placeholder tools)
6. Ensure all existing accessibility analysis functionality is preserved

## User Stories

1. **As a user**, I want to collapse the entire sidebar via a button in the navbar so that I can maximize screen space for viewing the PDF when I don't need the tools.

2. **As a user**, I want to expand multiple tool panels at once so that I can compare information from different tools simultaneously.

3. **As a user**, I want to see the accessibility analysis in a dedicated foldout panel so that it's organized with other tools rather than taking up the entire sidebar.

4. **As a developer**, I want to add new tools to the sidebar by creating a simple template include so that extending functionality is straightforward and doesn't require modifying core sidebar logic.

5. **As a user**, I want each tool panel to expand downward without moving its header so that the interface feels stable and predictable.

## Demoable Units of Work

### Unit 1: Collapsible Sidebar with Single Static Foldout
**Purpose:** Establish the basic sidebar collapse/expand mechanism and prove the foldout component works.

**Demo Criteria:**
- Sidebar can be collapsed/expanded via a toggle button in the navbar
- When collapsed, sidebar shows a 40px wide vertical bar
- One static foldout tool is visible with placeholder content ("Tool 1")
- Foldout can be expanded/collapsed by clicking its header
- Foldout expands downward, pushing content below it

**Proof Artifacts:**
- URL: `http://localhost:8080/viewer/<pdf_id>/` (with any uploaded PDF)
- Screenshot showing: sidebar collapsed state (40px), sidebar expanded with foldout collapsed, sidebar expanded with foldout expanded
- Manual test: Click navbar toggle button, click foldout header, verify animations

### Unit 2: Accessibility Summary Migrated to Foldout
**Purpose:** Migrate existing functionality into the new architecture without losing features.

**Demo Criteria:**
- Accessibility analysis content appears in the first foldout
- All existing data displays correctly (errors, warnings, summary stats, structure info, metadata)
- Foldout is labeled "Accessibility Analysis"
- Default state: sidebar expanded, foldout collapsed

**Proof Artifacts:**
- URL: `http://localhost:8080/viewer/<pdf_id>/` (with a PDF that has accessibility data)
- Screenshot showing the accessibility foldout expanded with real data
- Verification: All fields from original implementation are present and styled correctly

### Unit 3: Complete Tool Sidebar with 6 Tools
**Purpose:** Demonstrate the composable architecture with all tool slots populated.

**Demo Criteria:**
- Sidebar contains 6 foldout tools total
- Tool 1: "Accessibility Analysis" (with real data)
- Tools 2-6: "Tool 2" through "Tool 6" (with placeholder content)
- Multiple tools can be expanded simultaneously
- Each tool has a distinct header and content area
- Template structure allows easy addition of new tools

**Proof Artifacts:**
- URL: `http://localhost:8080/viewer/<pdf_id>/`
- Screenshot showing multiple tools expanded at once
- Code walkthrough: Show how a developer would add "Tool 7" by creating a new template include
- Test: Expand all 6 tools, verify no layout issues and content grows unbounded

## Functional Requirements

### FR1: Sidebar Structure
1.1. The sidebar must maintain the existing `.left-toolbar` container with fixed width of 350px when expanded  
1.2. The sidebar must be collapsible via a toggle button in the navbar  
1.3. When collapsed, the sidebar must show a 40px wide vertical bar  
1.4. When expanded, the sidebar must display all tool foldouts  
1.5. The sidebar collapse state must default to expanded on page load  

### FR2: Navbar Toggle Button
2.1. A toggle button must be added to the navbar (top band) to control sidebar visibility  
2.2. The button must have a clear visual indicator (hamburger menu or sidebar icon)  
2.3. The button must be positioned consistently with other navbar elements  
2.4. The button must use inline SVG for its icon  
2.5. The button state must visually reflect whether the sidebar is collapsed or expanded  

### FR3: Foldout Component
3.1. Each foldout must consist of a header section and a content section  
3.2. The header must remain fixed in position when the foldout expands/collapses  
3.3. The content section must expand downward, pushing subsequent foldouts down  
3.4. Multiple foldouts must be able to be expanded simultaneously  
3.5. Clicking a foldout header must toggle its expanded/collapsed state  
3.6. All foldouts must default to collapsed state on page load  
3.7. The header must have a visual indicator (chevron SVG icon) showing expand/collapse state  
3.8. The header must be visually distinct from the content area (different background or border)  
3.9. Expanded foldout content must grow unbounded to fit all content (no max-height or scrolling)  

### FR4: Accessibility Analysis Tool
4.1. The first foldout must be labeled "Accessibility Analysis"  
4.2. All existing accessibility analysis content must be moved into this foldout's content area  
4.3. The following sections must be preserved: errors, warnings, summary, document structure, metadata  
4.4. All existing styling and data display logic must remain functional  
4.5. The foldout must display "No accessibility analysis available" when no data exists  

### FR5: Placeholder Tools
5.1. Five additional foldout tools must be created with labels "Tool 2" through "Tool 6"  
5.2. Each placeholder tool must contain simple placeholder content (e.g., "Content for Tool N coming soon")  
5.3. Placeholder tools must use the same foldout component structure as the accessibility tool  

### FR6: Composability & Extensibility
6.1. Each tool's content must be defined in a separate Django template file  
6.2. The main sidebar template must include tool templates using Django's `{% include %}` tag  
6.3. Adding a new tool must require only: creating a new template file and adding one include line  
6.4. Tool templates must accept context variables passed from the view  
6.5. The foldout wrapper must be reusable across all tools  

### FR7: Visual Design
7.1. Foldout headers must have hover states to indicate interactivity  
7.2. Expand/collapse transitions must be smooth (CSS transitions)  
7.3. The chevron SVG icon must rotate when expanding/collapsing  
7.4. Content areas must maintain existing styling from the current implementation  
7.5. All icons (navbar toggle, foldout chevrons) must use inline SVG  
7.6. The collapsed sidebar (40px) should provide a visual affordance that it can be expanded  

## Non-Goals (Out of Scope)

1. **Persistent State**: Foldout expanded/collapsed states will NOT be saved to localStorage or server-side
2. **Responsive/Mobile Design**: The sidebar will NOT be optimized for mobile devices or small screens
3. **Resizable Sidebar**: Users will NOT be able to drag to resize the sidebar width
4. **Drag-and-Drop Reordering**: Tools will NOT be reorderable by users
5. **Tool-Specific Backend Logic**: This spec covers only the UI structure; individual tool functionality (beyond accessibility analysis) is out of scope
6. **WebSocket/AJAX Implementation**: While tools will eventually communicate with the server, the communication mechanism is not part of this spec
7. **Keyboard Navigation**: Advanced keyboard shortcuts for tool navigation are not required (basic tab/enter accessibility is sufficient)
8. **Animation Preferences**: No settings for disabling animations or adjusting animation speed
9. **Internal Scrolling**: Foldout content will NOT have max-height constraints or internal scrollbars (tools that grow too large will eventually be converted to modal popups in future work)

## Design Considerations

### Template Structure
```
templates/
├── navbar.html (add sidebar toggle button)
├── server/
│   ├── viewer.html (main template)
│   └── tools/
│       ├── _tool_wrapper.html (reusable foldout component)
│       ├── accessibility_analysis.html (tool 1 content)
│       ├── tool_2.html (placeholder)
│       ├── tool_3.html (placeholder)
│       ├── tool_4.html (placeholder)
│       ├── tool_5.html (placeholder)
│       └── tool_6.html (placeholder)
```

### Foldout Component Pattern
Each tool should be wrapped in a reusable foldout structure:
```django
{% include "server/tools/_tool_wrapper.html" with tool_id="accessibility" tool_title="Accessibility Analysis" tool_content="server/tools/accessibility_analysis.html" %}
```

### CSS Classes
- `.sidebar` - Main sidebar container (replaces `.left-toolbar`)
- `.sidebar-collapsed` - Modifier class when sidebar is collapsed (40px width)
- `.sidebar-toggle` - Toggle button in navbar for collapsing/expanding sidebar
- `.tool-foldout` - Individual foldout container
- `.tool-header` - Clickable header section
- `.tool-content` - Expandable content section
- `.tool-content-expanded` - Modifier class when content is visible

### JavaScript Requirements
- Toggle sidebar collapse/expand (triggered from navbar button)
- Toggle individual foldout expand/collapse
- Rotate chevron SVG icons
- Smooth height transitions for content areas
- Update navbar toggle button state/icon

### SVG Icons
- **Navbar Toggle**: Hamburger menu or sidebar icon (3 horizontal lines or panel icon)
- **Foldout Chevron**: Right-pointing chevron (collapsed) / Down-pointing chevron (expanded)

## Technical Considerations

1. **Existing Code Preservation**: The current accessibility analysis logic in `server/views.py` (lines 50-65) must remain unchanged. Only the template structure changes.

2. **Django Template Inheritance**: Use Django's template system effectively with `{% include %}` for composability.

3. **CSS Transitions**: Use CSS transitions for smooth expand/collapse animations. Since content grows unbounded, use `max-height` with a large value or JavaScript to calculate actual height for smoother animations.

4. **JavaScript Vanilla**: Implement with vanilla JavaScript. Keep it simple and maintainable.

5. **Accessibility**: Ensure proper ARIA attributes for expand/collapse states (`aria-expanded`, `aria-controls`, `aria-labelledby`).

6. **Navbar Integration**: The toggle button must integrate cleanly with the existing navbar structure in `templates/navbar.html` without disrupting current layout.

7. **Collapsed Sidebar Visual**: The 40px collapsed sidebar should show a subtle visual cue (border, shadow, or background) to indicate it's interactive.

## Success Metrics

1. **Code Maintainability**: A developer can add a new tool by creating a single template file and adding one line to the main template (< 5 minutes of work).

2. **Feature Parity**: All existing accessibility analysis data displays correctly in the new foldout structure with no visual regressions.

3. **Performance**: Expanding/collapsing foldouts and the sidebar feels smooth with no janky animations or layout shifts.

4. **User Experience**: Users can easily understand how to collapse the sidebar (via navbar button) and expand individual tools without instructions.

5. **Scalability**: The unbounded content growth works well for current tools, with the understanding that future large-content tools will use modals.

## Open Questions

None remaining - all design decisions have been clarified:
- ✅ Sidebar toggle in navbar
- ✅ Collapsed width: 40px
- ✅ Icons: Inline SVG
- ✅ Content height: Grow unbounded (future large tools will use modals)
- ✅ Tool communication: No preference (deferred to future implementation)