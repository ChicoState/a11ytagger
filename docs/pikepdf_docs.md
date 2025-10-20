# pikepdf Documentation
# Extracted from https://pikepdf.readthedocs.io/en/latest/
# Generated for LLM consumption



---
# 
Source: https://pikepdf.readthedocs.io/en/latest/

# pikepdf Documentation[](#pikepdf-documentation)

A northern pike, or *esox lucius*.[](#id1)

**pikepdf** is a Python library allowing creation, manipulation and repair of
PDFs. It provides a Pythonic wrapper around the C++ PDF content transformation
library [qpdf](https://qpdf.org).

Python + qpdf = “py” + “qpdf” = “pyqpdf”, which looks like a dyslexia test and
is no fun to type. But say “pyqpdf” out loud, and it sounds like “pikepdf”.

## At a glance[](#at-a-glance)

pikepdf is a library intended for developers who want to create, manipulate, parse,
repair, and abuse the PDF format. It supports reading and write PDFs, including
creating from scratch. Thanks to qpdf, it supports linearizing PDFs and access
to encrypted PDFs.

```
# Rotate all pages in a file by 180 degrees
import pikepdf

with pikepdf.Pdf.open(&#39;test.pdf&#39;) as my_pdf:
    for page in my_pdf.pages:
        page.rotate(180, relative=True)
    my_pdf.save(&#39;test-rotated.pdf&#39;)

```

It is a low level library that requires knowledge of PDF internals and some
familiarity with the [PDF specification](https://opensource.adobe.com/dc-acrobat-sdk-docs/standards/pdfstandards/pdf/PDF32000_2008.pdf).
It does not provide a user interface of its own.

pikepdf would help you build apps that do things like:

Pike fish are tough, hard-fighting, aggressive predators.[](#id2)

- 
[Copy pages](topics/pages.html#copyother) from one PDF into another

- 
[Split](topics/pages.html#splitpdf) and [merge](topics/pages.html#mergepdf) PDFs

- 
Extract content from a PDF such as [images](topics/images.html#extract-image)

- 
Replace content, such as [replacing an image](topics/images.html#replace-image) without
altering the rest of the file

- 
Repair, reformat or [`linearize`](api/main.html#pikepdf.Pdf.save) PDFs

- 
Change the size of pages and reposition content

- 
Optimize PDFs similar to Acrobat’s features by downsampling images,
deduplicating

- 
Calculate how much to charge for a scanning project based on the materials
scanned

- 
Alter a PDF to meet a target specification such as PDF/A or PDF/X

- 
Add or modify PDF [metadata](topics/metadata.html#accessmetadata)

- 
Add, remove, extract, and modify PDF [attachments](topics/attachments.html#attachments)
(i.e. embedded files)

- 
Create well-formed but invalid PDFs for testing purposes

What it cannot do:

Pikemen bracing for a calvary charge, carrying pikes.[](#id3)

- 
Rasterize PDF pages for display (that is, produce an image that shows what
a PDF page looks like at a particular resolution/zoom level) – use
[PyMuPDF](https://github.com/pymupdf/PyMuPDF), [pypdfium2](https://github.com/pypdfium2-team/pypdfium2), [python-poppler](https://github.com/cbrunet/python-poppler) or [Ghostscript](https://github.com/ArtifexSoftware/ghostpdl) instead

- 
Convert from PDF to other similar paper capture formats like epub, XPS, DjVu,
Postscript – use [MuPDF](https://github.com/ArtifexSoftware/mupdf) or [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- 
Print to paper

If you only want to generate PDFs and not read or modify them, consider
reportlab (a “write-only” PDF generator).

### Requirements[](#requirements)

pikepdf currently requires **Python 3.9+**. pikepdf 1.x supports Python 3.5.
pikepdf 2.x and 3.x support Python 3.6; pikepdf 4.x through 6.x support Python
3.7; pikepdf 7.x through 9.x support Python 3.8.

### Similar libraries[](#similar-libraries)

Unlike similar Python libraries such as pypdf, pikepdf is not pure
Python. These libraries were designed prior to Python wheels which has made Python
extension libraries much easier to work with. By leveraging the existing mature
code base of qpdf, despite being new, pikepdf is already more capable than both
in many respects – for example, it can read compress object streams, repair
damaged PDFs in many cases, and linearize PDFs. Unlike those libraries, it’s not
pure Python: it is impure and proud of it.

PyMuPDF is a PDF library with impressive capabilities. However, its AGPL license
is much more restrictive than pikepdf, and its dependency on static libraries
makes it difficult to include in open source Linux or BSD distributions.

### In use[](#in-use)

pikepdf is used by the same author’s [OCRmyPDF](https://github.com/jbarlow83/OCRmyPDF) to inspect input PDFs, graft the
generated OCR layers on to page content, and output PDFs. Its code contains several
practical examples, particular in `pdfinfo.py`, `graft.py`, and
`optimize.py`. pikepdf is also used in its test suite.

Introduction

- [Installation](installation.html)
[Basic installation](installation.html#basic-installation)

- [Binary wheel availability](installation.html#binary-wheel-availability)

- [Platform support](installation.html#platform-support)

- [Installing on FreeBSD](installation.html#installing-on-freebsd)

- [PyPy3 support](installation.html#pypy3-support)

- [Building from source](source_build.html)
[Requirements](source_build.html#requirements)

- [  GCC or Clang, linking to system libraries](source_build.html#gcc-or-clang-linking-to-system-libraries)

- [  GCC or Clang and linking to user libraries](source_build.html#gcc-or-clang-and-linking-to-user-libraries)

- [  Building against a qpdf source tree](source_build.html#building-against-a-qpdf-source-tree)

- [ Building against a qpdf source tree](source_build.html#id1)

- [Building the documentation](source_build.html#building-the-documentation)

- [Tutorial](tutorial.html)
[Opening and saving PDFs](tutorial.html#opening-and-saving-pdfs)

- [Creating PDFs](tutorial.html#creating-pdfs)

- [Inspecting pages](tutorial.html#inspecting-pages)

- [PDF dictionaries](tutorial.html#pdf-dictionaries)

- [Page dictionaries](tutorial.html#page-dictionaries)

- [repr() output](tutorial.html#repr-output)

- [Item and attribute notation](tutorial.html#item-and-attribute-notation)

- [Deleting pages](tutorial.html#deleting-pages)

- [Saving changes](tutorial.html#saving-changes)

- [Next steps](tutorial.html#next-steps)

Release notes

- [Release notes](releasenotes/index.html)

Topics

- [PDF split, merge, and document assembly](topics/pages.html)
[Split a PDF into single page PDFs](topics/pages.html#split-a-pdf-into-single-page-pdfs)

- [Merge (concatenate) PDF from several PDFs](topics/pages.html#merge-concatenate-pdf-from-several-pdfs)

- [Reversing the order of pages](topics/pages.html#reversing-the-order-of-pages)

- [Copying pages from other PDFs](topics/pages.html#copying-pages-from-other-pdfs)

- [Copying pages within a PDF](topics/pages.html#copying-pages-within-a-pdf)

- [Using counting numbers](topics/pages.html#using-counting-numbers)

- [Accessing page labels](topics/pages.html#accessing-page-labels)

- [Pages information from Root](topics/pages.html#pages-information-from-root)

- [Working with pages](topics/page.html)
[Page boxes](topics/page.html#page-boxes)

- [Object model](topics/objects.html)
[Making PDF objects](topics/objects.html#making-pdf-objects)

- [Object lifecycle and memory management](topics/objects.html#object-lifecycle-and-memory-management)

- [Indirect objects](topics/objects.html#indirect-objects)

- [Object helpers](topics/objects.html#object-helpers)

- [Stream objects](topics/streams.html)
[Reading stream objects](topics/streams.html#reading-stream-objects)

- [Reading stream objects as a Python I/O streams](topics/streams.html#reading-stream-objects-as-a-python-i-o-streams)

- [Working with content streams](topics/content_streams.html)
[Pretty-printing content streams](topics/content_streams.html#pretty-printing-content-streams)

- [How content streams draw images](topics/content_streams.html#how-content-streams-draw-images)

- [Editing a content stream](topics/content_streams.html#editing-a-content-stream)

- [Editing content streams robustly](topics/content_streams.html#editing-content-streams-robustly)

- [Extracting text from PDFs](topics/content_streams.html#extracting-text-from-pdfs)

- [Interpreting and generating content streams](topics/content_streams.html#interpreting-and-generating-content-streams)

- [Working with images](topics/images.html)
[Playing with images](topics/images.html#playing-with-images)

- [Extracting images](topics/images.html#extracting-images)

- [Replacing an image](topics/images.html#replacing-an-image)

- [Removing an image](topics/images.html#removing-an-image)

- [Overlays, underlays, watermarks, n-up](topics/overlays.html)

- [Working with interactive forms](topics/interactive_forms.html)
[Extracting Form Data](topics/interactive_forms.html#extracting-form-data)

- [Inspecting the Form](topics/interactive_forms.html#inspecting-the-form)

- [Filling Form Data](topics/interactive_forms.html#filling-form-data)

- [Character encoding](topics/encoding.html)
[PDFDocEncoding](topics/encoding.html#pdfdocencoding)

- [Other codecs](topics/encoding.html#other-codecs)

- [Metadata](topics/metadata.html)
[Automatic metadata updates](topics/metadata.html#automatic-metadata-updates)

- [Accessing metadata](topics/metadata.html#accessing-metadata)

- [Removing metadata items](topics/metadata.html#removing-metadata-items)

- [Checking PDF/A conformance](topics/metadata.html#checking-pdf-a-conformance)

- [Notice for application developers](topics/metadata.html#notice-for-application-developers)

- [Low-level XMP metadata access](topics/metadata.html#low-level-xmp-metadata-access)

- [The Document Info dictionary](topics/metadata.html#the-document-info-dictionary)

- [Outlines](topics/outlines.html)
[Creating outlines](topics/outlines.html#creating-outlines)

- [Editing outlines](topics/outlines.html#editing-outlines)

- [Destinations](topics/outlines.html#destinations)

- [Outline structure](topics/outlines.html#outline-structure)

- [Name trees](topics/nametrees.html)

- [Attaching files to a PDF](topics/attachments.html)
[General notes on attached files](topics/attachments.html#general-notes-on-attached-files)

- [How to find attachments in a PDF viewer](topics/attachments.html#how-to-find-attachments-in-a-pdf-viewer)

- [Creating attachment annotations](topics/attachments.html#creating-attachment-annotations)

- [Default appearance in PDF viewers](topics/pagelayout.html)

- [PDF security](topics/security.html)
[Password security](topics/security.html#password-security)

- [PDF content restrictions](topics/security.html#pdf-content-restrictions)

- [Digital signatures and certificates](topics/security.html#digital-signatures-and-certificates)

API

- [Main objects](api/main.html)
[`Pdf`](api/main.html#pikepdf.Pdf)

- [`pikepdf.open()`](api/main.html#pikepdf.open)

- [`pikepdf.new()`](api/main.html#pikepdf.new)

- [Access modes](api/main.html#access-modes)

- [Object construction](api/main.html#object-construction)

- [Common PDF data structures](api/main.html#common-pdf-data-structures)

- [Content stream elements](api/main.html#content-stream-elements)

- [Internal objects](api/main.html#internal-objects)

- [Jobs](api/main.html#jobs)

- [Support models](api/models.html)
[`ObjectHelper`](api/models.html#pikepdf.ObjectHelper)

- [`Page`](api/models.html#pikepdf.Page)

- [`PdfImage`](api/models.html#pikepdf.PdfImage)

- [`PdfInlineImage`](api/models.html#pikepdf.PdfInlineImage)

- [`PdfMetadata`](api/models.html#pikepdf.models.PdfMetadata)

- [`Encryption`](api/models.html#pikepdf.models.Encryption)

- [`Outline`](api/models.html#pikepdf.models.Outline)

- [`OutlineItem`](api/models.html#pikepdf.models.OutlineItem)

- [`Permissions`](api/models.html#pikepdf.Permissions)

- [`EncryptionInfo`](api/models.html#pikepdf.models.EncryptionInfo)

- [`AcroForm`](api/models.html#pikepdf.AcroForm)

- [`AcroFormField`](api/models.html#pikepdf.AcroFormField)

- [`Annotation`](api/models.html#pikepdf.Annotation)

- [`Attachments`](api/models.html#pikepdf._core.Attachments)

- [`AttachedFileSpec`](api/models.html#pikepdf.AttachedFileSpec)

- [`AttachedFile`](api/models.html#pikepdf._core.AttachedFile)

- [`NameTree`](api/models.html#pikepdf.NameTree)

- [`NumberTree`](api/models.html#pikepdf.NumberTree)

- [Canvas](api/canvas.html)
[`Canvas`](api/canvas.html#pikepdf.canvas.Canvas)

- [`_CanvasAccessor`](api/canvas.html#pikepdf.canvas._CanvasAccessor)

- [`ContentStreamBuilder`](api/canvas.html#pikepdf.canvas.ContentStreamBuilder)

- [`LoadedImage`](api/canvas.html#pikepdf.canvas.LoadedImage)

- [Text and fonts](api/canvas.html#text-and-fonts)

- [Form](api/form.html)
[`Form`](api/form.html#pikepdf.form.Form)

- [Form Fields](api/form.html#form-fields)

- [Generating Appearance Streams](api/form.html#generating-appearance-streams)

- [Content streams](api/filters.html)
[Content stream parsers](api/filters.html#content-stream-parsers)

- [Content stream token filters](api/filters.html#content-stream-token-filters)

- [Exceptions](api/exceptions.html)
[`PdfError`](api/exceptions.html#pikepdf.exceptions.PdfError)

- [`PasswordError`](api/exceptions.html#pikepdf.exceptions.PasswordError)

- [`ForeignObjectError`](api/exceptions.html#pikepdf.exceptions.ForeignObjectError)

- [`OutlineStructureError`](api/exceptions.html#pikepdf.exceptions.OutlineStructureError)

- [`UnsupportedImageTypeError`](api/exceptions.html#pikepdf.exceptions.UnsupportedImageTypeError)

- [`HifiPrintImageNotTranscodableError`](api/exceptions.html#pikepdf.exceptions.HifiPrintImageNotTranscodableError)

- [`InvalidPdfImageError`](api/exceptions.html#pikepdf.exceptions.InvalidPdfImageError)

- [`DataDecodingError`](api/exceptions.html#pikepdf.exceptions.DataDecodingError)

- [`DeletedObjectError`](api/exceptions.html#pikepdf.exceptions.DeletedObjectError)

- [`DependencyError`](api/exceptions.html#pikepdf.exceptions.DependencyError)

- [`PdfParsingError`](api/exceptions.html#pikepdf.exceptions.PdfParsingError)

- [`ImageDecompressionError`](api/exceptions.html#pikepdf.exceptions.ImageDecompressionError)

- [Settings](api/settings.html)
[`get_decimal_precision()`](api/settings.html#pikepdf.settings.get_decimal_precision)

- [`set_decimal_precision()`](api/settings.html#pikepdf.settings.set_decimal_precision)

- [`set_flate_compression_level()`](api/settings.html#pikepdf.settings.set_flate_compression_level)

Reference

- [Architecture](references/arch.html)
[Internals](references/arch.html#internals)

- [Thread safety](references/arch.html#thread-safety)

- [File handles](references/arch.html#file-handles)

- [Build process notes](references/build_process.html)
[macOS crypto provider](references/build_process.html#macos-crypto-provider)

- [macOS generally](references/build_process.html#macos-generally)

- [Contributing guidelines](references/contributing.html)
[Big changes](references/contributing.html#big-changes)

- [Code style: Python](references/contributing.html#code-style-python)

- [Code style: C++](references/contributing.html#code-style-c)

- [Adding C++ code](references/contributing.html#adding-c-code)

- [Tests](references/contributing.html#tests)

- [New dependencies](references/contributing.html#new-dependencies)

- [English style guide](references/contributing.html#english-style-guide)

- [Known ports/packagers](references/contributing.html#known-ports-packagers)

- [Debugging](references/debugging.html)
[Using gdb to debug C++ and Python](references/debugging.html#using-gdb-to-debug-c-and-python)

- [Compiling a debug build of qpdf](references/debugging.html#compiling-a-debug-build-of-qpdf)

- [Compile and link against qpdf source tree](references/debugging.html#compile-and-link-against-qpdf-source-tree)

- [Enabling qpdf tracing](references/debugging.html#enabling-qpdf-tracing)

- [Valgrind](references/debugging.html#valgrind)

- [Profiling pikepdf](references/debugging.html#profiling-pikepdf)

- [pymemtrace](references/debugging.html#pymemtrace)

- [Resources](references/resources.html)

---
# Main
Source: https://pikepdf.readthedocs.io/en/latest/api/main.html

# Main objects[](#main-objects)

*class *pikepdf.Pdf(**args*, ***kwargs*)[](#pikepdf.Pdf)
: 

*property *Root*: [Object](#pikepdf.Object)*[](#pikepdf.Pdf.Root)

**Return type:**

[Object](#pikepdf.Object)

*property *acroform*: [AcroForm](models.html#pikepdf.AcroForm)*[](#pikepdf.Pdf.acroform)
: 
Returns a helper object for working with interactive forms.

Tip

This creates a new AcroForm helper object each time this property is
used. If you’re planning on doing multiple form-related operations,
keep a reference to this object. The helper has an internal cache
that can speed up certain operations.

**Return type:**

[AcroForm](models.html#pikepdf.AcroForm)

add_blank_page(***, *page_size=...*)[](#pikepdf.Pdf.add_blank_page)
: 
Add a blank page to this PDF.

If pages already exist, the page will be added to the end. Pages may be
reordered using `Pdf.pages`.

The caller may add content to the page by modifying its objects after creating
it.

**Parameters:**

**page_size** (*tuple*) – The size of the page in PDF units (1/72 inch or 0.35mm).
Default size is set to a US Letter 8.5” x 11” page.

**Return type:**
: 
[Page](models.html#pikepdf.Page)

*property *allow*: pikepdf.models.encryption.Permissions*[](#pikepdf.Pdf.allow)
: 
Report permissions associated with this PDF.

By default these permissions will be replicated when the PDF is
saved. Permissions may also only be changed when a PDF is being saved,
and are only available for encrypted PDFs. If a PDF is not encrypted,
all operations are reported as allowed.

pikepdf has no way of enforcing permissions.

**Return type:**

pikepdf.models.encryption.Permissions

*property *attachments*: [Attachments](models.html#pikepdf._core.Attachments)*[](#pikepdf.Pdf.attachments)
: 
Returns a mapping that provides access to all files attached to this PDF.

PDF supports attaching (or embedding, if you prefer) any other type of file,
including other PDFs. This property provides read and write access to
these objects by filename.

**Return type:**

[Attachments](models.html#pikepdf._core.Attachments)

check()[](#pikepdf.Pdf.check)
: 

**Return type:**

list[str]

check_linearization(*stream=...*)[](#pikepdf.Pdf.check_linearization)
: 
Reports information on the PDF’s linearization.

**Parameters:**

**stream** (*object*) – A stream to write this information too; must
implement `.write()` and `.flush()` method. Defaults to
`sys.stderr`.

**Returns:**
: 
`True` if the file is correctly linearized, and `False` if
the file is linearized but the linearization data contains errors
or was incorrectly generated.

**Raises:**
: 
**RuntimeError** – If the PDF in question is not linearized at all.

**Return type:**
: 
bool

check_pdf_syntax()[](#pikepdf.Pdf.check_pdf_syntax)
: 
Check if PDF is syntactically well-formed.

Similar to `qpdf --check`, checks for syntax
or structural problems in the PDF. This is mainly useful to PDF
developers and may not be informative to the average user. PDFs with
these problems still render correctly, if PDF viewers are capable of
working around the issues they contain. In many cases, pikepdf can
also fix the problems.

Unlike `qpdf --check`, this function does not check for linearization
issues (see `check_linearization()`) and some other issues. To
replicate the exact behavior of qpdf’s check in pikepdf, use
`pikepdf.Job(['pikepdf', '--check', 'input.pdf']).run()`.

An example problem found by this function is a xref table that is
missing an object reference. A page dictionary with the wrong type of
key, such as a string instead of an array of integers for its mediabox,
is not the sort of issue checked for. If this were an XML checker, it
would tell you if the XML is well-formed, but could not tell you if
the XML is valid XHTML or if it can be rendered as a usable web page.

This function also attempts to decompress all streams in the PDF.
If no JBIG2 decoder is available and JBIG2 images are presented,
a warning will occur that JBIG2 cannot be checked.

This function returns a list of strings describing the issues. The
text is subject to change and should not be treated as a stable API.

**Returns:**

Empty list if no issues were found. List of issues as text strings
if issues were found.

**Return type:**
: 
list[str]

close()[](#pikepdf.Pdf.close)
: 
Close a `Pdf` object and release resources acquired by pikepdf.

If pikepdf opened the file handle it will close it (e.g. when opened with a file
path). If the caller opened the file for pikepdf, the caller close the file.
`with` blocks will call close when exit.

pikepdf lazily loads data from PDFs, so some [`pikepdf.Object`](#pikepdf.Object) may
implicitly depend on the [`pikepdf.Pdf`](#pikepdf.Pdf) being open. This is always the
case for [`pikepdf.Stream`](#pikepdf.Stream) but can be true for any object. Do not close
the Pdf object if you might still be accessing content from it.

When an `Object` is copied from one `Pdf` to another, the `Object` is
copied into the destination `Pdf` immediately, so after accessing all desired
information from the source `Pdf` it may be closed.

Changed in version 3.0: In pikepdf 2.x, this function actually worked by resetting to a very short
empty PDF. Code that relied on this quirk may not function correctly.

**Return type:**

None

copy_foreign(*h*)[](#pikepdf.Pdf.copy_foreign)
: 
Copy an `Object` from a foreign `Pdf` and return a copy.

The object must be owned by a different `Pdf` from this one.

If the object has previously been copied, return a reference to
the existing copy, even if that copy has been modified in the meantime.

If you want to copy a page from one PDF to another, use:
`pdf_b.pages[0] = pdf_a.pages[0]`. That interface accounts for the
complexity of copying pages.

This function is used to copy a [`pikepdf.Object`](#pikepdf.Object) that is owned by
some other `Pdf` into this one. This is performs a deep (recursive) copy
and preserves all references that may exist in the foreign object. For
example, if

```
&gt;&gt;&gt; object_a = pdf.copy_foreign(object_x)
&gt;&gt;&gt; object_b = pdf.copy_foreign(object_y)
&gt;&gt;&gt; object_c = pdf.copy_foreign(object_z)

```

and `object_z` is a shared descendant of both `object_x` and `object_y`
in the foreign PDF, then `object_c` is a shared descendant of both
`object_a` and `object_b` in this PDF. If `object_x` and `object_y`
refer to the same object, then `object_a` and `object_b` are the
same object.

It also copies all [`pikepdf.Stream`](#pikepdf.Stream) objects. Since this may copy
a large amount of data, it is not done implicitly. This function does
not copy references to pages in the foreign PDF - it stops at page
boundaries. Thus, if you use `copy_foreign()` on a table of contents
(`/Outlines` dictionary), you may have to update references to pages.

Direct objects, including dictionaries, do not need `copy_foreign()`.
pikepdf will automatically convert and construct them.

Note

pikepdf automatically treats incoming pages from a foreign PDF as
foreign objects, so [`Pdf.pages`](#pikepdf.Pdf.pages) does not require this treatment.

See also

[QPDF::copyForeignObject](https://qpdf.readthedocs.io/en/stable/design.html#copying-objects-from-other-pdf-files)

Changed in version 2.1: Error messages improved.

**Parameters:**

**h** ([*Object*](#pikepdf.Object))

**Return type:**
: 
[Object](#pikepdf.Object)

*property *docinfo*: pikepdf.objects.Dictionary*[](#pikepdf.Pdf.docinfo)
: 
Access the (deprecated) document information dictionary.

The document information dictionary is a brief metadata record that can
store some information about the origin of a PDF. It is deprecated and
removed in the PDF 2.0 specification (not deprecated from the
perspective of pikepdf). Use the `.open_metadata()` API instead, which
will edit the modern (and unfortunately, more complicated) XMP metadata
object and synchronize changes to the document information dictionary.

This property simplifies access to the actual document information
dictionary and ensures that it is created correctly if it needs to be
created.

A new, empty dictionary will be created if this property is accessed
and dictionary does not exist or the wrong object type exists at that
location. (This is to ensure that convenient code
like `pdf.docinfo[Name.Title] = &quot;Title&quot;` will work when the dictionary
does not exist at all.) This dictionary is always indirect.

You can delete the document information dictionary by deleting this property,
`del pdf.docinfo`. Note that accessing the property after deleting it
will re-create with a new, empty dictionary.

Changed in version 2.4: Added support for `del pdf.docinfo`.

**Return type:**

pikepdf.objects.Dictionary

*property *encryption*: pikepdf.models.encryption.EncryptionInfo*[](#pikepdf.Pdf.encryption)
: 
Report encryption information for this PDF.

Encryption settings may only be changed when a PDF is saved.

**Return type:**

pikepdf.models.encryption.EncryptionInfo

*property *extension_level*: int*[](#pikepdf.Pdf.extension_level)
: 
Returns the extension level of this PDF.

If a developer has released multiple extensions of a PDF version against
the same base version value, they shall increase the extension level
by 1. To be interpreted with [`pdf_version`](#pikepdf.Pdf.pdf_version).

**Return type:**

int

*property *filename*: str*[](#pikepdf.Pdf.filename)
: 
The source filename of an existing PDF, when available.

When the Pdf was created from scratch, this returns ‘empty PDF’.
When the Pdf was created from a stream, the return value is the
word ‘stream’ followed by some information about the stream, if
available.

**Return type:**

str

flatten_annotations(*mode*)[](#pikepdf.Pdf.flatten_annotations)
: 
Flattens all PDF annotations into regular PDF content.

Annotations are markup such as review comments, highlights, proofreading
marks. User data entered into interactive form fields also counts as an
annotation.

When annotations are flattened, they are “burned into” the regular
content stream of the document and the fact that they were once annotations
is deleted. This can be useful when preparing a document for printing,
to ensure annotations are printed, or to finalize a form that should
no longer be changed.

**Parameters:**

**mode** (*str*) – One of the strings `'all'`, `'screen'`, `'print'`. If
omitted or  set to empty, treated as `'all'`. `'screen'`
flattens all except those marked with the PDF flag /NoView.
`'print'` flattens only those marked for printing.
Default is `'all'`.

**Return type:**
: 
None

Added in version 2.11.

generate_appearance_streams()[](#pikepdf.Pdf.generate_appearance_streams)
: 
Generates appearance streams for AcroForm forms and form fields.

Appearance streams describe exactly how annotations and form fields
should appear to the user. If omitted, the PDF viewer is free to
render the annotations and form fields according to its own settings,
as needed.

For every form field in the document, this generates appearance
streams, subject to the limitations of qpdf’s ability to create
appearance streams.

When invoked, this method will modify the `Pdf` in memory. It may be
best to do this after the `Pdf` is opened, or before it is saved,
because it may modify objects that the user does not expect to be
modified.

If `Pdf.Root.AcroForm.NeedAppearances` is `False` or not present, no
action is taken (because no appearance streams need to be generated).
If `True`, the appearance streams are generated, and the NeedAppearances
flag is set to `False`.

**See:**
[https://github.com/qpdf/qpdf/blob/bf6b9ba1c681a6fac6d585c6262fb2778d4bb9d2/include/qpdf/QPDFFormFieldObjectHelper.hh#L216](https://github.com/qpdf/qpdf/blob/bf6b9ba1c681a6fac6d585c6262fb2778d4bb9d2/include/qpdf/QPDFFormFieldObjectHelper.hh#L216)

Added in version 2.11.

**Return type:**
: 
None

get_object(*objgen: tuple[int, int]*) &#x2192; [Object](#pikepdf.Object)[](#pikepdf.Pdf.get_object)
: 
Retrieve an object from the PDF.

Can be called with either a 2-tuple of (objid, gen) or
two integers objid and gen.

get_warnings()[](#pikepdf.Pdf.get_warnings)
: 

**Return type:**

list

*property *is_encrypted*: bool*[](#pikepdf.Pdf.is_encrypted)
: 
Returns True if the PDF is encrypted.

For information about the nature of the encryption, see
[`Pdf.encryption`](#pikepdf.Pdf.encryption).

**Return type:**

bool

*property *is_linearized*: bool*[](#pikepdf.Pdf.is_linearized)
: 
Returns True if the PDF is linearized.

Specifically returns True iff the file starts with a linearization
parameter dictionary.  Does no additional validation.

**Return type:**

bool

make_indirect(*obj*)[](#pikepdf.Pdf.make_indirect)
: 
Attach an object to the Pdf as an indirect object.

Direct objects appear inline in the binary encoding of the PDF.
Indirect objects appear inline as references (in English, “look
up object 4 generation 0”) and then read from another location in
the file. The PDF specification requires that certain objects
are indirect - consult the PDF specification to confirm.

Generally a resource that is shared should be attached as an
indirect object. [`pikepdf.Stream`](#pikepdf.Stream) objects are always
indirect, and creating them will automatically attach it to the
Pdf.

**Parameters:**

**obj** (*T*) – The object to attach. If this a [`pikepdf.Object`](#pikepdf.Object),
it will be attached as an indirect object. If it is
any other Python object, we attempt conversion to
[`pikepdf.Object`](#pikepdf.Object) attach the result. If the
object is already an indirect object, a reference to
the existing object is returned. If the `pikepdf.Object`
is owned by a different Pdf, an exception is raised; use
`pikepdf.Object.copy_foreign()` instead.

**Return type:**
: 
T

See also

[`pikepdf.Object.is_indirect()`](#pikepdf.Object.is_indirect)

make_stream(*data*, *d=None*, ***kwargs*)[](#pikepdf.Pdf.make_stream)
: 
Create a new pikepdf.Stream object that is attached to this PDF.

**See:**
[`pikepdf.Stream.__new__()`](#pikepdf.Stream.__new__)

**Parameters:**
: 
**data** (*bytes*)

**Return type:**
: 
pikepdf.objects.Stream

*classmethod *new()[](#pikepdf.Pdf.new)
: 
Create a new, empty PDF.

This is best when you are constructing a PDF from scratch.

In most cases, if you are working from an existing PDF, you should open the
PDF using [`pikepdf.Pdf.open()`](#pikepdf.Pdf.open) and transform it, instead of a creating
a new one, to preserve metadata and structural information. For example,
if you want to split a PDF into two parts, you should open the PDF and
transform it into the desired parts, rather than creating a new PDF and
copying pages into it.

**Return type:**

[Pdf](#pikepdf.Pdf)

*property *objects*: [_ObjectList](#pikepdf._core._ObjectList)*[](#pikepdf.Pdf.objects)
: 
Return an iterable list of all objects in the PDF.

After deleting content from a PDF such as pages, objects related
to that page, such as images on the page, may still be present in
this list.

**Return type:**

[_ObjectList](#pikepdf._core._ObjectList)

*static *open(*filename_or_stream*, ***, *password=''*, *hex_password=False*, *ignore_xref_streams=False*, *suppress_warnings=True*, *attempt_recovery=True*, *inherit_page_attributes=True*, *access_mode=AccessMode.default*, *allow_overwriting_input=False*)[](#pikepdf.Pdf.open)
: 
Open an existing file at *filename_or_stream*.

If *filename_or_stream* is path-like, the file will be opened for reading. The
file should not be modified by another process while it is open in pikepdf, or
undefined behavior may occur. This is because the file may be lazily loaded.
When `.close()` is called, the file handle that pikepdf opened will be closed.

If *filename_or_stream* is stream, the data will be accessed as a readable
binary stream, from the current position in that stream.  When pdf =
Pdf.open(stream) is called on a stream, pikepdf will not call
`stream.close()`; the caller must call both `pdf.close()` and
`stream.close()`, in that order, when the Pdf and stream are no longer needed.
Use with-blocks will call `.close()` automatically.

Whether a file or stream is opened, you must ensure that the data is not
modified by another thread or process, or undefined behavior will occur. You
also may not overwrite the input file using `.save()`, unless
`allow_overwriting_input=True`. This is because data may be lazily loaded.

If you intend to edit the file in place, or want to protect the file against
modification by another process, use `allow_overwriting_input=True`. This
tells pikepdf to make a private copy of the file.

Any changes to the file must be persisted by using `.save()`.

Examples

```
&gt;&gt;&gt; with Pdf.open(&quot;test.pdf&quot;) as pdf:
...     pass

```

```
&gt;&gt;&gt; pdf = Pdf.open(&quot;test.pdf&quot;, password=&quot;rosebud&quot;)

```

**Parameters:**

- 
**filename_or_stream** (*pathlib.Path** | **str** | **BinaryIO*) – Filename or Python readable and seekable file
stream of PDF to open.

- 
**password** (*str** | **bytes*) – User or owner password to open an
encrypted PDF. If the type of this parameter is `str` it will be
encoded as UTF-8. If the type is `bytes` it will be saved verbatim.
Passwords are always padded or truncated to 32 bytes internally. Use
ASCII passwords for maximum compatibility.

- 
**hex_password** (*bool*) – If True, interpret the password as a
hex-encoded version of the exact encryption key to use, without
performing the normal key computation. Useful in forensics.

- 
**ignore_xref_streams** (*bool*) – If True, ignore cross-reference
streams. See qpdf documentation.

- 
**suppress_warnings** (*bool*) – If True (default), warnings are not
printed to stderr. Use [`pikepdf.Pdf.get_warnings()`](#pikepdf.Pdf.get_warnings) to retrieve
warnings.

- 
**attempt_recovery** (*bool*) – If True (default), attempt to recover
from PDF parsing errors.

- 
**inherit_page_attributes** (*bool*) – If True (default), push attributes
set on a group of pages to individual pages

- 
**access_mode** (*AccessMode*) – If `.default`, pikepdf will
decide how to access the file. Currently, it will always selected stream
access. To attempt memory mapping and fallback to stream if memory
mapping failed, use `.mmap`.  Use `.mmap_only` to require memory
mapping or fail (this is expected to only be useful for testing).
Applications should be prepared to handle the SIGBUS signal on POSIX in
the event that the file is successfully mapped but later goes away.

- 
**allow_overwriting_input** (*bool*) – If True, allows calling `.save()`
to overwrite the input file. This is performed by loading the entire
input file into memory at open time; this will use more memory and may
recent performance especially when the opened file will not be modified.

**Raises:**
: 

- 
**pikepdf.PasswordError** – If the password failed to open the
file.

- 
**pikepdf.PdfError** – If for other reasons we could not open
the file.

- 
**TypeError** – If the type of `filename_or_stream` is not
usable.

- 
**FileNotFoundError** – If the file was not found.

**Return type:**
: 
[Pdf](#pikepdf.Pdf)

Note

When *filename_or_stream* is a stream and the stream is located on a
network, pikepdf assumes that the stream using buffering and read caches to
achieve reasonable performance. Streams that fetch data over a network in
response to every read or seek request, no matter how small, will perform
poorly. It may be easier to download a PDF from network to temporary local
storage (such as `io.BytesIO`), manipulate it, and then re-upload it.

Changed in version 3.0: Keyword arguments now mandatory for everything except the first
argument.

open_metadata(*set_pikepdf_as_editor=True*, *update_docinfo=True*, *strict=False*)[](#pikepdf.Pdf.open_metadata)
: 
Open the PDF’s XMP metadata for editing.

There is no `.close()` function on the metadata object, since this is
intended to be used inside a `with` block only.

For historical reasons, certain parts of PDF metadata are stored in
two different locations and formats. This feature coordinates edits so
that both types of metadata are updated consistently and “atomically”
(assuming single threaded access). It operates on the `Pdf` in memory,
not any file on disk. To persist metadata changes, you must still use
`Pdf.save()`.

Example

```
&gt;&gt;&gt; pdf = pikepdf.Pdf.open(&quot;../tests/resources/graph.pdf&quot;)
&gt;&gt;&gt; with pdf.open_metadata() as meta:
...     meta[&#39;dc:title&#39;] = &#39;Set the Dublic Core Title&#39;
...     meta[&#39;dc:description&#39;] = &#39;Put the Abstract here&#39;

```

**Parameters:**

- 
**set_pikepdf_as_editor** (*bool*) – Automatically update the metadata `pdf:Producer`
to show that this version of pikepdf is the most recent software to
modify the metadata, and `xmp:MetadataDate` to timestamp the update.
Recommended, except for testing.

- 
**update_docinfo** (*bool*) – Update the standard fields of DocumentInfo
(the old PDF metadata dictionary) to match the corresponding
XMP fields. The mapping is described in
`PdfMetadata.DOCINFO_MAPPING`. Nonstandard DocumentInfo
fields and XMP metadata fields with no DocumentInfo equivalent
are ignored.

- 
**strict** (*bool*) – If `False` (the default), we aggressively attempt
to recover from any parse errors in XMP, and if that fails we
overwrite the XMP with an empty XMP record.  If `True`, raise
errors when either metadata bytes are not valid and well-formed
XMP (and thus, XML). Some trivial cases that are equivalent to
empty or incomplete “XMP skeletons” are never treated as errors,
and always replaced with a proper empty XMP block. Certain
errors may be logged.

**Return type:**
: 
pikepdf.models.metadata.PdfMetadata

open_outline(*max_depth=15*, *strict=False*)[](#pikepdf.Pdf.open_outline)
: 
Open the PDF outline (“bookmarks”) for editing.

Recommend for use in a `with` block. Changes are committed to the
PDF when the block exits. (The `Pdf` must still be opened.)

Example

```
&gt;&gt;&gt; pdf = pikepdf.open(&#39;../tests/resources/outlines.pdf&#39;)
&gt;&gt;&gt; with pdf.open_outline() as outline:
...     outline.root.insert(0, pikepdf.OutlineItem(&#39;Intro&#39;, 0))

```

**Parameters:**

- 
**max_depth** (*int*) – Maximum recursion depth of the outline to be
imported and re-written to the document. `0` means only
considering the root level, `1` the first-level
sub-outline of each root element, and so on. Items beyond
this depth will be silently ignored. Default is `15`.

- 
**strict** (*bool*) – With the default behavior (set to `False`),
structural errors (e.g. reference loops) in the PDF document
will only cancel processing further nodes on that particular
level, recovering the valid parts of the document outline
without raising an exception. When set to `True`, any such
error will raise an `OutlineStructureError`, leaving the
invalid parts in place.
Similarly, outline objects that have been accidentally
duplicated in the `Outline` container will be silently
fixed (i.e. reproduced as new objects) or raise an
`OutlineStructureError`.

**Return type:**
: 
pikepdf.models.outlines.Outline

*property *owner_password_matched*: bool*[](#pikepdf.Pdf.owner_password_matched)
: 
Returns True if the owner password matched when the `Pdf` was opened.

It is possible for both the user and owner passwords to match.

Added in version 2.10.

**Return type:**

bool

*property *pages*: [PageList](#pikepdf._core.PageList)*[](#pikepdf.Pdf.pages)
: 
Returns the list of pages.

**Return type:**

[PageList](#pikepdf._core.PageList)

*property *pdf_version*: str*[](#pikepdf.Pdf.pdf_version)
: 
The version of the PDF specification used for this file, such as ‘1.7’.

More precise information about the PDF version can be opened from the
Pdf’s XMP metadata.

**Return type:**

str

remove_unreferenced_resources()[](#pikepdf.Pdf.remove_unreferenced_resources)
: 
Remove from /Resources any object not referenced in page’s contents.

PDF pages may share resource dictionaries with other pages. If
pikepdf is used for page splitting, pages may reference resources
in their /Resources dictionary that are not actually required.
This purges all unnecessary resource entries.

For clarity, if all references to any type of object are removed, that
object will be excluded from the output PDF on save. (Conversely, only
objects that are discoverable from the PDF’s root object are included.)
This function removes objects that are referenced from the page /Resources
dictionary, but never called for in the content stream, making them
unnecessary.

Suggested before saving, if content streams or /Resources dictionaries
are edited.

**Return type:**

None

*property *root*: [Object](#pikepdf.Object)*[](#pikepdf.Pdf.root)
: 
The /Root object of the PDF.

**Return type:**

[Object](#pikepdf.Object)

save(*filename_or_stream=None*, ***, *static_id=False*, *preserve_pdfa=True*, *min_version=''*, *force_version=''*, *fix_metadata_version=True*, *compress_streams=True*, *stream_decode_level=None*, *object_stream_mode=ObjectStreamMode.preserve*, *normalize_content=False*, *linearize=False*, *qdf=False*, *progress=None*, *encryption=None*, *recompress_flate=False*, *deterministic_id=False*)[](#pikepdf.Pdf.save)
: 
Save all modifications to this [`pikepdf.Pdf`](#pikepdf.Pdf).

**Parameters:**

- 
**filename_or_stream** (*pathlib.Path** | **str** | **BinaryIO** | **None*) – Where to write the output. If a file
exists in this location it will be overwritten.
If the file was opened with `allow_overwriting_input=True`,
then it is permitted to overwrite the original file, and
this parameter may be omitted to implicitly use the original
filename. Otherwise, the filename may not be the same as the
input file, as overwriting the input file would corrupt data
since pikepdf using lazy loading.

- 
**static_id** (*bool*) – Indicates that the `/ID` metadata, normally
calculated as a hash of certain PDF contents and metadata
including the current time, should instead be set to a static
value. Only use this for debugging and testing. Use
`deterministic_id` if you want to get the same `/ID` for
the same document contents.

- 
**preserve_pdfa** (*bool*) – Ensures that the file is generated in a
manner compliant with PDF/A and other stricter variants.
This should be True, the default, in most cases.

- 
**min_version** (*str** | **tuple**[**str**, **int**]*) – Sets the minimum version of PDF
specification that should be required. If left alone qpdf
will decide. If a tuple, the second element is an integer, the
extension level. If the version number is not a valid format,
qpdf will decide what to do.

- 
**force_version** (*str** | **tuple**[**str**, **int**]*) – Override the version recommend by qpdf,
potentially creating an invalid file that does not display
in old versions. See qpdf manual for details. If a tuple, the
second element is an integer, the extension level.

- 
**fix_metadata_version** (*bool*) – If `True` (default) and the XMP metadata
contains the optional PDF version field, ensure the version in
metadata is correct. If the XMP metadata does not contain a PDF
version field, none will be added. To ensure that the field is
added, edit the metadata and insert a placeholder value in
`pdf:PDFVersion`. If XMP metadata does not exist, it will
not be created regardless of the value of this argument.

- 
**object_stream_mode** ([*ObjectStreamMode*](#pikepdf.ObjectStreamMode)) – `disable` prevents the use of object streams.
`preserve` keeps object streams from the input file.
`generate` uses object streams wherever possible,
creating the smallest files but requiring PDF 1.5+.

- 
**compress_streams** (*bool*) – 
Enables or disables the compression of
uncompressed stream objects. By default this is set to
`True`, and the only reason to set it to `False` is for
debugging or inspecting PDF contents.

When enabled, uncompressed stream objects will be compressed
whether they were uncompressed in the PDF when it was opened,
or when the user creates new [`pikepdf.Stream`](#pikepdf.Stream) objects
attached to the PDF. Stream objects can also be created
indirectly, such as when content from another PDF is merged
into the one being saved.

Only stream objects that have no compression will be
compressed when this object is set. If the object is
compressed, compression will be preserved.

Setting compress_streams=False does not trigger decompression
unless decompression is specifically requested by setting
both `compress_streams=False` and `stream_decode_level`
to the desired decode level (e.g. `.generalized` will
decompress most non-image content).

This option does not trigger recompression of existing
compressed streams. For that, use `recompress_flate`.

The XMP metadata stream object, if present, is never
compressed, to facilitate metadata reading by parsers that
don’t understand the full structure of PDF.

- 
**stream_decode_level** ([*StreamDecodeLevel*](#pikepdf.StreamDecodeLevel)* | **None*) – Specifies how
to encode stream objects. See documentation for
[`pikepdf.StreamDecodeLevel`](#pikepdf.StreamDecodeLevel).

- 
**recompress_flate** (*bool*) – When disabled (the default), qpdf does not
uncompress and recompress streams compressed with the Flate
compression algorithm. If True, pikepdf will instruct qpdf to
do this, which may be useful if recompressing streams to a
higher compression level.

- 
**normalize_content** (*bool*) – Enables parsing and reformatting the
content stream within PDFs. This may debugging PDFs easier.

- 
**linearize** (*bool*) – Enables creating linear or “fast web view”,
where the file’s contents are organized sequentially so that
a viewer can begin rendering before it has the whole file.
As a drawback, it tends to make files larger.

- 
**qdf** (*bool*) – Save output QDF mode.  QDF mode is a special output
mode in qpdf to allow editing of PDFs in a text editor. Use
the program `fix-qdf` to fix convert back to a standard
PDF.

- 
**progress** (*Callable**[**[**int**]**, **None**] **| **None*) – Specify a callback function that is called
as the PDF is written. The function will be called with an
integer between 0-100 as the sole parameter, the progress
percentage. This function may not access or modify the PDF
while it is being written, or data corruption will almost
certainly occur.

- 
**encryption** (*pikepdf.models.encryption.Encryption** | **bool** | **None*) – If `False`
or omitted, existing encryption will be removed. If `True`
encryption settings are copied from the originating PDF.
Alternately, an `Encryption` object may be provided that
sets the parameters for new encryption.

- 
**deterministic_id** (*bool*) – Indicates that the `/ID` metadata, normally
calculated as a hash of certain PDF contents and metadata
including the current time, should instead be computed using
only deterministic data like the file contents. At a small
runtime cost, this enables generation of the same `/ID` if
the same inputs are converted in the same way multiple times.
Does not work for encrypted files.

**Raises:**
: 

- 
[**PdfError**](exceptions.html#pikepdf.exceptions.PdfError) – 

- 
[**ForeignObjectError**](exceptions.html#pikepdf.exceptions.ForeignObjectError) – 

- 
**ValueError** – 

**Return type:**
: 
None

You may call `.save()` multiple times with different parameters
to generate different versions of a file, and you *may* continue
to modify the file after saving it. `.save()` does not modify
the `Pdf` object in memory, except possibly by updating the XMP
metadata version with `fix_metadata_version`.

Note

[`pikepdf.Pdf.remove_unreferenced_resources()`](#pikepdf.Pdf.remove_unreferenced_resources) before saving
may eliminate unnecessary resources from the output file if there
are any objects (such as images) that are referenced in a page’s
Resources dictionary but never called in the page’s content stream.

Note

pikepdf can read PDFs with incremental updates, but always
coalesces any incremental updates into a single non-incremental
PDF file when saving.

Note

If filename_or_stream is a stream and the process is interrupted during
writing, the stream may be left in a corrupt state. It is the
responsibility of the caller to manage the stream in this case.

Changed in version 2.7: Added *recompress_flate*.

Changed in version 3.0: Keyword arguments now mandatory for everything except the first
argument.

Changed in version 8.1: If filename_or_stream is a filename and that file exists, the new file
is written to a temporary file in the same directory and then moved into
place. This prevents the existing destination file from being corrupted
if the process is interrupted during writing; previously, corrupting the
destination file was possible. If no file exists at the destination, output
is written directly to the destination, but the destination will be deleted
if errors occur during writing. Prior to 8.1, the file was always written
directly to the destination, which could result in a corrupt destination
file if the process was interrupted during writing.

Changed in version 9.1: When opened with `allow_overwriting_input=True`, we now attempt to
restore the original file permissions, ownership and creation time.
The modified time is always set to the time of saving. An unusual
umask or other settings changes still cause a failure to restore
permissions.

show_xref_table()[](#pikepdf.Pdf.show_xref_table)
: 
Pretty-print the Pdf’s xref (cross-reference table).

**Return type:**

None

*property *trailer*: [Object](#pikepdf.Object)*[](#pikepdf.Pdf.trailer)
: 
Provides access to the PDF trailer object.

See {{ pdfrm }} section 7.5.5. Generally speaking,
the trailer should not be modified with pikepdf, and modifying it
may not work. Some of the values in the trailer are automatically
changed when a file is saved.

**Return type:**

[Object](#pikepdf.Object)

*property *user_password_matched*: bool*[](#pikepdf.Pdf.user_password_matched)
: 
Returns True if the user password matched when the `Pdf` was opened.

It is possible for both the user and owner passwords to match.

Added in version 2.10.

**Return type:**

bool

pikepdf.open()[](#pikepdf.open)
: 
Alias for [`pikepdf.Pdf.open()`](#pikepdf.Pdf.open).

pikepdf.new()[](#pikepdf.new)
: 
Alias for [`pikepdf.Pdf.new()`](#pikepdf.Pdf.new).

## Access modes[](#access-modes)

*class *pikepdf.ObjectStreamMode(**args*, ***kwds*)[](#pikepdf.ObjectStreamMode)
: 
Options for saving object streams within PDFs.

Object streams are more a compact
way of saving certain types of data that was added in PDF 1.5. All
modern PDF viewers support object streams, but some third party tools
and libraries cannot read them.

disable*: int** = Ellipsis*[](#pikepdf.ObjectStreamMode.disable)

Disable the use of object streams.

If any object streams exist in the file, remove them when the file is saved.

generate*: int** = Ellipsis*[](#pikepdf.ObjectStreamMode.generate)
: 
Preserve any existing object streams in the original file.

This is the default behavior.

preserve*: int** = Ellipsis*[](#pikepdf.ObjectStreamMode.preserve)
: 
Generate object streams.

*class *pikepdf.StreamDecodeLevel(**args*, ***kwds*)[](#pikepdf.StreamDecodeLevel)
: 
Options for decoding streams within PDFs.

all*: int** = Ellipsis*[](#pikepdf.StreamDecodeLevel.all)

Do not attempt to apply any filters. Streams
remain as they appear in the original file. Note that
uncompressed streams may still be compressed on output. You can
disable that by saving with `.save(..., compress_streams=False)`.

generalized*: int** = Ellipsis*[](#pikepdf.StreamDecodeLevel.generalized)
: 
This is the default. libqpdf will apply
LZWDecode, ASCII85Decode, ASCIIHexDecode, and FlateDecode
filters on the input. When saved with
`compress_streams=True`, the default, the effect of this
is that streams filtered with these older and less efficient
filters will be recompressed with the Flate filter. As a
special case, if a stream is already compressed with
FlateDecode and `compress_streams=True`, the original
compressed data will be preserved.

none*: int** = Ellipsis*[](#pikepdf.StreamDecodeLevel.none)
: 
In addition to uncompressing the
generalized compression formats, supported non-lossy
compression will also be be decoded. At present, this includes
the RunLengthDecode filter.

specialized*: int** = Ellipsis*[](#pikepdf.StreamDecodeLevel.specialized)
: 
In addition to generalized and non-lossy
specialized filters, supported lossy compression filters will
be applied. At present, this includes DCTDecode (JPEG)
compression. Note that compressing the resulting data with
DCTDecode again will accumulate loss, so avoid multiple
compression and decompression cycles. This is mostly useful for
(low-level) retrieving image data; see [`pikepdf.PdfImage`](models.html#pikepdf.PdfImage) for
the preferred method.

*class *pikepdf.Encryption[](#pikepdf.Encryption)
: 
Specify the encryption settings to apply when a PDF is saved.

R*: Literal[2, 3, 4, 5, 6]** = 6*[](#pikepdf.Encryption.R)

Select the security handler algorithm to use. Choose from:
`2`, `3`, `4` or `6`. By default, the highest version of
is selected (`6`). `5` is a deprecated algorithm that should
not be used.

aes*: bool** = True*[](#pikepdf.Encryption.aes)
: 
If True, request the AES algorithm. If False, use RC4.
If omitted, AES is selected whenever possible (R &gt;= 4).

allow*: [Permissions](models.html#pikepdf.Permissions)*[](#pikepdf.Encryption.allow)
: 
The permissions to set.
If omitted, all permissions are granted to the user.

metadata*: bool** = True*[](#pikepdf.Encryption.metadata)
: 
If True, also encrypt the PDF metadata. If False,
metadata is not encrypted. Reading document metadata without
decryption may be desirable in some cases. Requires `aes=True`.
If omitted, metadata is encrypted whenever possible.

owner*: str** = ''*[](#pikepdf.Encryption.owner)
: 
The owner password to use. This allows full control
of the file. If blank, the PDF will be encrypted and
present as “(SECURED)” in PDF viewers. If the owner password
is blank, the user password should be as well.

user*: str** = ''*[](#pikepdf.Encryption.user)
: 
The user password to use. With this password, some
restrictions will be imposed by a typical PDF reader.
If blank, the PDF can be opened by anyone, but only modified
as allowed by the permissions in `allow`.

## Object construction[](#object-construction)

*class *pikepdf.Object[](#pikepdf.Object)
: 

__bool__()[](#pikepdf.Object.__bool__)

**Return type:**

bool

__bytes__()[](#pikepdf.Object.__bytes__)
: 

**Return type:**

bytes

__contains__(*obj*)[](#pikepdf.Object.__contains__)
: 

**Parameters:**

**obj** ([*Object*](#pikepdf.Object)* | **str*)

**Return type:**
: 
bool

__copy__()[](#pikepdf.Object.__copy__)
: 

**Return type:**

[Object](#pikepdf.Object)

__delattr__(*name*)[](#pikepdf.Object.__delattr__)
: 

**Parameters:**

**name** (*str*)

**Return type:**
: 
None

__delitem__(*name*)[](#pikepdf.Object.__delitem__)
: 

**Parameters:**

**name** (*str** | **pikepdf.objects.Name** | **int*)

**Return type:**
: 
None

__dir__()[](#pikepdf.Object.__dir__)
: 

**Return type:**

list

__eq__(*other*)[](#pikepdf.Object.__eq__)
: 

**Parameters:**

**other** (*Any*)

**Return type:**
: 
bool

__float__()[](#pikepdf.Object.__float__)
: 

**Return type:**

float

__getattr__(*name*)[](#pikepdf.Object.__getattr__)
: 

**Parameters:**

**name** (*str*)

**Return type:**
: 
[Object](#pikepdf.Object)

__getitem__(*name*)[](#pikepdf.Object.__getitem__)
: 

**Parameters:**

**name** (*str** | **pikepdf.objects.Name** | **int*)

**Return type:**
: 
[Object](#pikepdf.Object)

__hash__()[](#pikepdf.Object.__hash__)
: 

**Return type:**

int

__int__()[](#pikepdf.Object.__int__)
: 

**Return type:**

int

__iter__()[](#pikepdf.Object.__iter__)
: 

**Return type:**

collections.abc.Iterable[[Object](#pikepdf.Object)]

__len__()[](#pikepdf.Object.__len__)
: 

**Return type:**

int

__setattr__(*name*, *value*)[](#pikepdf.Object.__setattr__)
: 

**Parameters:**

- 
**name** (*str*)

- 
**value** (*Any*)

**Return type:**
: 
None

__setitem__(*name*, *value*)[](#pikepdf.Object.__setitem__)
: 

**Parameters:**

- 
**name** (*str** | **pikepdf.objects.Name** | **int*)

- 
**value** (*Any*)

**Return type:**
: 
None

append(*pyitem*)[](#pikepdf.Object.append)
: 
Append another object to an array; fails if the object is not an array.

**Parameters:**

**pyitem** (*Any*)

**Return type:**
: 
None

as_dict()[](#pikepdf.Object.as_dict)
: 

**Return type:**

_ObjectMapping

as_list()[](#pikepdf.Object.as_list)
: 

**Return type:**

[_ObjectList](#pikepdf._core._ObjectList)

emplace(*other*, *retain=...*)[](#pikepdf.Object.emplace)
: 
Copy all items from other without making a new object.

Particularly when working with pages, it may be desirable to remove all
of the existing page’s contents and emplace (insert) a new page on top
of it, in a way that preserves all links and references to the original
page. (Or similarly, for other Dictionary objects in a PDF.)

Any Dictionary keys in the iterable *retain* are preserved. By default,
/Parent is retained.

When a page is assigned (`pdf.pages[0] = new_page`), only the
application knows if references to the original the original page are
still valid. For example, a PDF optimizer might restructure a page
object into another visually similar one, and references would be valid;
but for a program that reorganizes page contents such as a N-up
compositor, references may not be valid anymore.

This method takes precautions to ensure that child objects in common
with `self` and `other` are not inadvertently deleted.

Example

```
&gt;&gt;&gt; pdf = pikepdf.Pdf.open(&#39;../tests/resources/fourpages.pdf&#39;)
&gt;&gt;&gt; pdf.pages[0].objgen
(3, 0)
&gt;&gt;&gt; pdf.pages[0].emplace(pdf.pages[1])
&gt;&gt;&gt; pdf.pages[0].objgen
(3, 0)
&gt;&gt;&gt; # Same object

```

Changed in version 2.11.1: Added the *retain* argument.

**Parameters:**

- 
**other** ([*Object*](#pikepdf.Object))

- 
**retain** (*collections.abc.Iterable**[**pikepdf.objects.Name**]*)

**Return type:**
: 
None

extend(*iter*)[](#pikepdf.Object.extend)
: 
Extend a pikepdf.Array with an iterable of other pikepdf.Object.

**Parameters:**

**iter** (*collections.abc.Iterable**[*[*Object*](#pikepdf.Object)*]*)

**Return type:**
: 
None

get(*key*, *default=...*)[](#pikepdf.Object.get)
: 
Retrieve an attribute from the object.

Only works if the object is a Dictionary, Array or Stream.

**Parameters:**

- 
**key** (*int** | **str** | **pikepdf.objects.Name*)

- 
**default** (*T** | **None*)

**Return type:**
: 
[Object](#pikepdf.Object) | T | None

get_raw_stream_buffer()[](#pikepdf.Object.get_raw_stream_buffer)
: 
Return a buffer protocol buffer describing the raw, encoded stream.

**Return type:**

Buffer

get_stream_buffer(*decode_level=...*)[](#pikepdf.Object.get_stream_buffer)
: 
Return a buffer protocol buffer describing the decoded stream.

**Parameters:**

**decode_level** ([*StreamDecodeLevel*](#pikepdf.StreamDecodeLevel))

**Return type:**
: 
Buffer

*property *images*: _ObjectMapping*[](#pikepdf.Object.images)
: 

**Return type:**

_ObjectMapping

*property *is_indirect*: bool*[](#pikepdf.Object.is_indirect)
: 
Returns True if the object is an indirect object.

**Return type:**

bool

is_owned_by(*possible_owner*)[](#pikepdf.Object.is_owned_by)
: 
Test if this object is owned by the indicated *possible_owner*.

**Parameters:**

**possible_owner** ([*Pdf*](#pikepdf.Pdf))

**Return type:**
: 
bool

*property *is_rectangle*: bool*[](#pikepdf.Object.is_rectangle)
: 
Returns True if the object is a rectangle (an array of 4 numbers).

**Return type:**

bool

items()[](#pikepdf.Object.items)
: 

**Return type:**

collections.abc.Iterable[tuple[str, [Object](#pikepdf.Object)]]

keys()[](#pikepdf.Object.keys)
: 
Get the keys of the object, if it is a Dictionary or Stream.

**Return type:**

set[str]

*property *objgen*: tuple[int, int]*[](#pikepdf.Object.objgen)
: 
Return the object-generation number pair for this object.

If this is a direct object, then the returned value is `(0, 0)`.
By definition, if this is an indirect object, it has a “objgen”,
and can be looked up using this in the cross-reference (xref) table.
Direct objects cannot necessarily be looked up.

The generation number is usually 0, except for PDFs that have been
incrementally updated. Incrementally updated PDFs are now uncommon,
since it does not take too long for modern CPUs to reconstruct an
entire PDF. pikepdf will consolidate all incremental updates
when saving.

**Return type:**

tuple[int, int]

*static *parse(*stream*, *description=...*)[](#pikepdf.Object.parse)
: 
Parse PDF binary representation into PDF objects.

**Parameters:**

- 
**stream** (*bytes*)

- 
**description** (*str*)

**Return type:**
: 
[Object](#pikepdf.Object)

read_bytes(*decode_level=...*)[](#pikepdf.Object.read_bytes)
: 
Decode and read the content stream associated with this object.

**Parameters:**

**decode_level** ([*StreamDecodeLevel*](#pikepdf.StreamDecodeLevel))

**Return type:**
: 
bytes

read_raw_bytes()[](#pikepdf.Object.read_raw_bytes)
: 
Read the content stream associated with a Stream, without decoding.

**Return type:**

bytes

same_owner_as(*other*)[](#pikepdf.Object.same_owner_as)
: 
Test if two objects are owned by the same [`pikepdf.Pdf`](#pikepdf.Pdf).

**Parameters:**

**other** ([*Object*](#pikepdf.Object))

**Return type:**
: 
bool

*property *stream_dict*: pikepdf.objects.Dictionary*[](#pikepdf.Object.stream_dict)
: 
Access the dictionary key-values for a [`pikepdf.Stream`](#pikepdf.Stream).

**Return type:**

pikepdf.objects.Dictionary

to_json(*dereference=...*, *schema_version=...*)[](#pikepdf.Object.to_json)
: 
Convert to a qpdf JSON representation of the object.

See the qpdf manual for a description of its JSON representation.
[https://qpdf.readthedocs.io/en/stable/json.html#qpdf-json-format](https://qpdf.readthedocs.io/en/stable/json.html#qpdf-json-format)

Not necessarily compatible with other PDF-JSON representations that
exist in the wild.

- 
Names are encoded as UTF-8 strings

- 
Indirect references are encoded as strings containing `obj gen R`

- 

**Strings are encoded as UTF-8 strings with unrepresentable binary**
characters encoded as `\uHHHH`

- 

**Encoding streams just encodes the stream’s dictionary; the stream**: 
data is not represented

- 

**Object types that are only valid in content streams (inline**: 
image, operator) as well as “reserved” objects are not
representable and will be serialized as `null`.

**Parameters:**
: 

- 
**dereference** (*bool*) – If True, dereference the object if this is an
indirect object.

- 
**schema_version** (*int*) – The version of the JSON schema. Defaults to 2.

**Returns:**
: 
JSON bytestring of object. The object is UTF-8 encoded
and may be decoded to a Python str that represents the binary
values `\x00-\xFF` as `U+0000` to `U+00FF`; that is,
it may contain mojibake.

**Return type:**
: 
bytes

Changed in version 6.0: Added *schema_version*.

unparse(*resolved=...*)[](#pikepdf.Object.unparse)
: 
Convert PDF objects into their binary representation.

Set resolved=True to deference indirect objects where possible.

If you want to unparse content streams, which are a collection of
objects that need special treatment, use
[`pikepdf.unparse_content_stream()`](filters.html#pikepdf.unparse_content_stream) instead.

Returns `bytes()` that can be used with [`Object.parse()`](#pikepdf.Object.parse)
to reconstruct the `pikepdf.Object`. If reconstruction is not possible,
a relative object reference is returned, such as `4 0 R`.

**Parameters:**

**resolved** (*bool*) – If True, deference indirect objects where possible.

**Return type:**
: 
bytes

with_same_owner_as(*arg0*)[](#pikepdf.Object.with_same_owner_as)
: 
Returns an object that is owned by the same Pdf that owns *other* object.

If the objects already have the same owner, this object is returned.
If the *other* object has a different owner, then a copy is created
that is owned by *other*’s owner. If this object is a direct object
(no owner), then an indirect object is created that is owned by
*other*. An exception is thrown if *other* is a direct object.

This method may be convenient when a reference to the Pdf is not
available.

Added in version 2.14.

**Parameters:**

**arg0** ([*Object*](#pikepdf.Object))

**Return type:**
: 
[Object](#pikepdf.Object)

wrap_in_array()[](#pikepdf.Object.wrap_in_array)
: 
Return the object wrapped in an array if not already an array.

**Return type:**

pikepdf.objects.Array

write(*data*, ***, *filter=...*, *decode_parms=...*, *type_check=...*)[](#pikepdf.Object.write)
: 
Replace stream object’s data with new (possibly compressed) data.

filter and decode_parms describe any compression that is already
present on the input data. For example, if your data is already
compressed with the Deflate algorithm, you would set
`filter=Name.FlateDecode`.

When writing the PDF in [`pikepdf.Pdf.save()`](#pikepdf.Pdf.save),
pikepdf may change the compression or apply compression to data that was
not compressed, depending on the parameters given to that function. It
will never change lossless to lossy encoding.

PNG and TIFF images, even if compressed, cannot be directly inserted
into a PDF and displayed as images.

**Parameters:**

- 
**data** (*bytes*) – the new data to use for replacement

- 
**filter** (*pikepdf.objects.Name** | **pikepdf.objects.Array** | **list**[**pikepdf.objects.Name**] **| **None*) – The filter(s) with which the
data is (already) encoded

- 
**decode_parms** (*pikepdf.objects.Dictionary** | **pikepdf.objects.Array** | **None*) – Parameters for the
filters with which the object is encode

- 
**type_check** (*bool*) – Check arguments; use False only if you want to
intentionally create malformed PDFs.

**Return type:**
: 
None

If only one filter is specified, it may be a name such as
Name(‘/FlateDecode’). If there are multiple filters, then array
of names should be given.

If there is only one filter, decode_parms is a Dictionary of
parameters for that filter. If there are multiple filters, then
decode_parms is an Array of Dictionary, where each array index
is corresponds to the filter.

*class *pikepdf.Name[](#pikepdf.Name)
: 
Construct a PDF Name object.

Names can be constructed with two notations:

- 
`Name.Resources`

- 
`Name('/Resources')`

The two are semantically equivalent. The former is preferred for names
that are normally expected to be in a PDF. The latter is preferred for
dynamic names and attributes.

__new__(*name*)[](#pikepdf.Name.__new__)

Construct a PDF Name.

**Parameters:**

**name** (*str** | *[*Name*](#pikepdf.Name))

**Return type:**
: 
[Name](#pikepdf.Name)

*classmethod *random(*len_=16*, *prefix=''*)[](#pikepdf.Name.random)
: 
Generate a cryptographically strong, random, valid PDF Name.

If you are inserting a new name into a PDF (for example,
name for a new image), you can use this function to generate a
cryptographically strong random name that is almost certainly already
not already in the PDF, and not colliding with other existing names.

This function uses Python’s secrets.token_urlsafe, which returns a
URL-safe encoded random number of the desired length. An optional
*prefix* may be prepended. (The encoding is ultimately done with
`base64.urlsafe_b64encode()`.) Serendipitously, URL-safe is also
PDF-safe.

When the length parameter is 16 (16 random bytes or 128 bits), the result
is probably globally unique and can be treated as never colliding with
other names.

The length of the returned string may vary because it is encoded,
but will always have `8 * len_` random bits.

**Parameters:**

- 
**len** – The length of the random string.

- 
**prefix** (*str*) – A prefix to prepend to the random string.

- 
**len_** (*int*)

**Return type:**
: 
[Name](#pikepdf.Name)

*class *pikepdf.String[](#pikepdf.String)
: 
Construct a PDF String object.

__new__(*s*)[](#pikepdf.String.__new__)

Construct a PDF String.

**Parameters:**

**s** (*str** | **bytes*) – The string to use. String will be encoded for
PDF, bytes will be constructed without encoding.

**Return type:**
: 
[String](#pikepdf.String)

*class *pikepdf.Array[](#pikepdf.Array)
: 
Construct a PDF Array object.

__new__(*a=None*)[](#pikepdf.Array.__new__)

Construct a PDF Array.

**Parameters:**

**a** (*collections.abc.Iterable** | **pikepdf._core.Rectangle** | **pikepdf._core.Matrix** | **None*) – An iterable of objects. All objects must be either
pikepdf.Object or convertible to pikepdf.Object.

**Return type:**
: 
[Array](#pikepdf.Array)

*class *pikepdf.Dictionary[](#pikepdf.Dictionary)
: 
Construct a PDF Dictionary object.

__new__(*d=None*, ***kwargs*)[](#pikepdf.Dictionary.__new__)

Construct a PDF Dictionary.

Works from either a Python `dict` or keyword arguments.

These two examples are equivalent:

```
pikepdf.Dictionary({&#39;/NameOne&#39;: 1, &#39;/NameTwo&#39;: &#39;Two&#39;})

pikepdf.Dictionary(NameOne=1, NameTwo=&#39;Two&#39;)

```

In either case, the keys must be strings, and the strings
correspond to the desired Names in the PDF Dictionary. The values
must all be convertible to pikepdf.Object.

**Parameters:**

**d** (*collections.abc.Mapping** | **None*)

**Return type:**
: 
[Dictionary](#pikepdf.Dictionary)

*class *pikepdf.Stream[](#pikepdf.Stream)
: 
Construct a PDF Stream object.

__new__(*owner*, *data=None*, *d=None*, ***kwargs*)[](#pikepdf.Stream.__new__)

Create a new stream object.

Streams stores arbitrary binary data and may or may not be compressed.
It also may or may not be a page or Form XObject’s content stream.

A stream dictionary is like a pikepdf.Dictionary or Python dict, except
it has a binary payload of data attached. The dictionary describes
how the data is compressed or encoded.

The dictionary may be initialized just like pikepdf.Dictionary is initialized,
using a mapping object or keyword arguments.

**Parameters:**

- 
**owner** ([*pikepdf.Pdf*](#pikepdf.Pdf)) – The Pdf to which this stream shall be attached.

- 
**data** (*bytes** | **None*) – The data bytes for the stream.

- 
**d** – An optional mapping object that will be used to construct the stream’s
dictionary.

- 
**kwargs** – Keyword arguments that will define the stream dictionary. Do not set
/Length here as pikepdf will manage this value. Set /Filter
if the data is already encoded in some format.

**Return type:**
: 
[Stream](#pikepdf.Stream)

Examples

**Using kwargs:**: 
```
&gt;&gt;&gt; pdf = pikepdf.Pdf.new()
&gt;&gt;&gt; s1 = pikepdf.Stream(
...     pdf,
...     b&quot;uncompressed image data&quot;,
...     BitsPerComponent=8,
...     ColorSpace=pikepdf.Name.DeviceRGB,
... )

```

**Using dict:**: 
```
&gt;&gt;&gt; pdf = pikepdf.Pdf.new()
&gt;&gt;&gt; d = pikepdf.Dictionary(Key1=1, Key2=2)
&gt;&gt;&gt; s2 = pikepdf.Stream(
...     pdf,
...     b&quot;data&quot;,
...     d
... )

```

Changed in version 2.2: Support creation of `pikepdf.Stream` from existing dictionary.

Changed in version 3.0: `obj` argument was removed; use `data`.

*class *pikepdf.Operator[](#pikepdf.Operator)
: 
Construct an operator for use in a content stream.

An Operator is one of a limited set of commands that can appear in PDF content
streams (roughly the mini-language that draws objects, lines and text on a
virtual PDF canvas). The commands [`parse_content_stream()`](filters.html#pikepdf.parse_content_stream) and
[`unparse_content_stream()`](filters.html#pikepdf.unparse_content_stream) create and expect Operators respectively, along
with their operands.

pikepdf uses the special Operator “INLINE IMAGE” to denote an inline image
in a content stream.

__new__(*name*)[](#pikepdf.Operator.__new__)

Construct an operator.

**Parameters:**

**name** (*str*)

**Return type:**
: 
[Operator](#pikepdf.Operator)

## Common PDF data structures[](#common-pdf-data-structures)

*class *pikepdf.Matrix[](#pikepdf.Matrix)
: 
A 2D affine matrix for PDF transformations.

PDF uses matrices to transform document coordinates to screen/device
coordinates.

PDF matrices are encoded as [`pikepdf.Array`](#pikepdf.Array) with exactly
six numeric elements, ordered as `a b c d e f`.

\[\begin{split}\begin{bmatrix}
a &amp; b &amp; 0 \\
c &amp; d &amp; 0 \\
e &amp; f &amp; 1 \\
\end{bmatrix}\end{split}\]

The approximate interpretation of these six parameters is documented
below. The values (0, 0, 1) in the third column are fixed, so a
general 3×3 matrix cannot be converted to a PDF matrix.

PDF transformation matrices are the transpose of most textbook
treatments.  In a textbook, typically `A × vc` is used to
transform a column vector `vc=(x, y, 1)` by the affine matrix `A`.
In PDF, the matrix is the transpose of that in the textbook,
and `vr × A'` is used to transform a row vector `vr=(x, y, 1)`.

Transformation matrices specify the transformation from the new
(transformed) coordinate system to the original (untransformed)
coordinate system. x’ and y’ are the coordinates in the
*untransformed* coordinate system, and x and y are the
coordinates in the *transformed* coordinate system.

PDF order:

\[\begin{split}\begin{equation}
\begin{bmatrix}
x' &amp; y' &amp; 1
\end{bmatrix}
=
\begin{bmatrix}
x &amp; y &amp; 1
\end{bmatrix}
\begin{bmatrix}
a &amp; b &amp; 0 \\
c &amp; d &amp; 0 \\
e &amp; f &amp; 1
\end{bmatrix}
\end{equation}\end{split}\]

To concatenate transformations, use the matrix multiple (`&#64;`)
operator to **pre**-multiply the next transformation onto existing
transformations.

Alternatively, use the .translated(), .scaled(), and .rotated()
methods to chain transformation operations.

Addition and other operations are not implemented because they’re not
that meaningful in a PDF context.

Matrix objects are immutable. All transformation methods return
new matrix objects.

Added in version 8.7.

__array__(*dtype=None*, *copy=True*)[](#pikepdf.Matrix.__array__)

Convert this matrix to a NumPy array of type dtype.

If copy is True, a copy is made. If copy is False, an exception is raised.

If numpy is not installed, this will throw an exception.

**Parameters:**

- 
**dtype** (*Any*)

- 
**copy** (*bool** | **None*)

**Return type:**
: 
numpy.ndarray

__init__()[](#pikepdf.Matrix.__init__)
: 

__matmul__(*other*)[](#pikepdf.Matrix.__matmul__)
: 
Return the matrix product of two matrices.

Can be used to concatenate transformations. Transformations should be
composed by **pre**-multiplying matrices. For example, to apply a
scaling transform, one could do:

```
scale = pikepdf.Matrix(2, 0, 0, 2, 0, 0)
scaled = scale @ matrix

```

**Parameters:**

**other** ([*Matrix*](#pikepdf.Matrix))

**Return type:**
: 
[Matrix](#pikepdf.Matrix)

*property *a*: float*[](#pikepdf.Matrix.a)
: 
`a` is the horizontal scaling factor.

**Return type:**

float

as_array()[](#pikepdf.Matrix.as_array)
: 
Convert this matrix to a pikepdf.Array.

A Matrix cannot be inserted into a PDF directly. Use this function
to convert a Matrix to a pikepdf.Array, which can be inserted.

**Return type:**

pikepdf.objects.Array

*property *b*: float*[](#pikepdf.Matrix.b)
: 
`b` is horizontal skewing.

**Return type:**

float

*property *c*: float*[](#pikepdf.Matrix.c)
: 
`c` is vertical skewing.

**Return type:**

float

*property *d*: float*[](#pikepdf.Matrix.d)
: 
`d` is the vertical scaling factor.

**Return type:**

float

*property *e*: float*[](#pikepdf.Matrix.e)
: 
`e` is the horizontal translation.

**Return type:**

float

encode()[](#pikepdf.Matrix.encode)
: 
Encode matrix to bytes suitable for including in a PDF content stream.

**Return type:**

bytes

*property *f*: float*[](#pikepdf.Matrix.f)
: 
`f` is the vertical translation.

**Return type:**

float

*classmethod *identity()[](#pikepdf.Matrix.identity)
: 
Construct an identity matrix.

More explicit than the constructor.

Added in version 9.7.0.

**Return type:**

[Matrix](#pikepdf.Matrix)

inverse()[](#pikepdf.Matrix.inverse)
: 
Return the inverse of the matrix.

The inverse matrix reverses the transformation of the original matrix.

In rare situations, the inverse may not exist. In that case, an
exception is thrown. The PDF will likely have rendering problems.

**Return type:**

[Matrix](#pikepdf.Matrix)

rotated(*angle_degrees_ccw*)[](#pikepdf.Matrix.rotated)
: 
Return a rotated copy of this matrix.

Calculates
`Matrix(cos(angle), sin(angle), -sin(angle), cos(angle), 0, 0) &#64; self`.

**Parameters:**

**angle_degrees_ccw** – angle in degrees counterclockwise

**Return type:**
: 
[Matrix](#pikepdf.Matrix)

scaled(*sx*, *sy*)[](#pikepdf.Matrix.scaled)
: 
Return a scaled copy of this matrix.

Calculates `Matrix(sx, 0, 0, sy, 0, 0) &#64; self`.

**Parameters:**

- 
**sx** – horizontal scaling

- 
**sy** – vertical scaling

**Return type:**
: 
[Matrix](#pikepdf.Matrix)

*property *shorthand*: tuple[float, float, float, float, float, float]*[](#pikepdf.Matrix.shorthand)
: 
Return the 6-tuple (a,b,c,d,e,f) that describes this matrix.

**Return type:**

tuple[float, float, float, float, float, float]

transform(*point: tuple[float, float]*) &#x2192; tuple[float, float][](#pikepdf.Matrix.transform)
: 

translated(*tx*, *ty*)[](#pikepdf.Matrix.translated)
: 
Return a translated copy of this matrix.

Calculates `Matrix(1, 0, 0, 1, tx, ty) &#64; self`.

**Parameters:**

- 
**tx** – horizontal translation

- 
**ty** – vertical translation

**Return type:**
: 
[Matrix](#pikepdf.Matrix)

*class *pikepdf.Rectangle(*llx: float*, *lly: float*, *urx: float*, *ury: float*, */*)[](#pikepdf.Rectangle)
: 
A PDF rectangle.

Typically this will be a rectangle in PDF units (points, 1/72”).
Unlike raster graphics, the rectangle is defined by the **lower**
left and upper right points.

Rectangles in PDF are encoded as [`pikepdf.Array`](#pikepdf.Array) with exactly
four numeric elements, ordered as `llx lly urx ury`.
See {{ pdfrm }} section 7.9.5.

The rectangle may be considered degenerate if the lower left corner
is not strictly less than the upper right corner.

Added in version 2.14.

Changed in version 8.5: Added operators to test whether rectangle `a` is contained in
rectangle `b` (`a &lt;= b`) and to calculate their intersection
(`a &amp; b`).

__and__(*other*)[](#pikepdf.Rectangle.__and__)

Return the bounding Rectangle of the common area of self and other.

**Parameters:**

**other** ([*Rectangle*](#pikepdf.Rectangle))

**Return type:**
: 
[Rectangle](#pikepdf.Rectangle)

__init__(*llx: float*, *lly: float*, *urx: float*, *ury: float*, */*) &#x2192; None[](#pikepdf.Rectangle.__init__)
: 
Construct a new rectangle.

as_array()[](#pikepdf.Rectangle.as_array)
: 
Returns this rectangle as a [`pikepdf.Array`](#pikepdf.Array).

**Return type:**

pikepdf.objects.Array

*property *height*: float*[](#pikepdf.Rectangle.height)
: 
The height of the rectangle.

**Return type:**

float

llx*: float** = Ellipsis*[](#pikepdf.Rectangle.llx)
: 
The lower left corner on the x-axis.

lly*: float** = Ellipsis*[](#pikepdf.Rectangle.lly)
: 
The lower left corner on the y-axis.

*property *lower_left*: tuple[float, float]*[](#pikepdf.Rectangle.lower_left)
: 
A point for the lower left corner.

**Return type:**

tuple[float, float]

*property *lower_right*: tuple[float, float]*[](#pikepdf.Rectangle.lower_right)
: 
A point for the lower right corner.

**Return type:**

tuple[float, float]

*property *upper_left*: tuple[float, float]*[](#pikepdf.Rectangle.upper_left)
: 
A point for the upper left corner.

**Return type:**

tuple[float, float]

*property *upper_right*: tuple[float, float]*[](#pikepdf.Rectangle.upper_right)
: 
A point for the upper right corner.

**Return type:**

tuple[float, float]

urx*: float** = Ellipsis*[](#pikepdf.Rectangle.urx)
: 
The upper right corner on the x-axis.

ury*: float** = Ellipsis*[](#pikepdf.Rectangle.ury)
: 
The upper right corner on the y-axis.

*property *width*: float*[](#pikepdf.Rectangle.width)
: 
The width of the rectangle.

**Return type:**

float

## Content stream elements[](#content-stream-elements)

*class *pikepdf.ContentStreamInstruction(*operands: [_ObjectList](#pikepdf._core._ObjectList)*, *operator: pikepdf.objects.Operator*)[](#pikepdf.ContentStreamInstruction)
: 
Represents one complete instruction inside a content stream.

*property *operands*: [_ObjectList](#pikepdf._core._ObjectList)*[](#pikepdf.ContentStreamInstruction.operands)

**Return type:**

[_ObjectList](#pikepdf._core._ObjectList)

*property *operator*: pikepdf.objects.Operator*[](#pikepdf.ContentStreamInstruction.operator)
: 

**Return type:**

pikepdf.objects.Operator

*class *pikepdf.ContentStreamInlineImage[](#pikepdf.ContentStreamInlineImage)
: 
Represents an instruction to draw an inline image.

pikepdf consolidates the BI-ID-EI sequence of operators, as appears in a PDF to
declare an inline image, and replaces them with a single virtual content stream
instruction with the operator “INLINE IMAGE”.

*property *iimage*: pikepdf.models.image.PdfInlineImage*[](#pikepdf.ContentStreamInlineImage.iimage)

**Return type:**

pikepdf.models.image.PdfInlineImage

*property *operands*: [_ObjectList](#pikepdf._core._ObjectList)*[](#pikepdf.ContentStreamInlineImage.operands)
: 

**Return type:**

[_ObjectList](#pikepdf._core._ObjectList)

*property *operator*: pikepdf.objects.Operator*[](#pikepdf.ContentStreamInlineImage.operator)
: 

**Return type:**

pikepdf.objects.Operator

## Internal objects[](#internal-objects)

These objects are returned by other pikepdf objects. They are part of the API,
but not intended to be created explicitly.

*class *pikepdf._core.PageList[](#pikepdf._core.PageList)
: 
For accessing pages in a PDF.

A `list`-like object enumerating a range of pages in a [`pikepdf.Pdf`](#pikepdf.Pdf).
It may be all of the pages or a subset. Obtain using [`pikepdf.Pdf.pages`](#pikepdf.Pdf.pages).

See [`pikepdf.Page`](models.html#pikepdf.Page) for accessing individual pages.

append(*page*)[](#pikepdf._core.PageList.append)

Add another page to the end.

While this method copies pages from one document to another, it does not
copy certain metadata such as annotations, form fields, bookmarks or
structural tree elements. Copying these is a more complex, application
specific operation.

**Parameters:**

**page** ([*Page*](models.html#pikepdf.Page))

**Return type:**
: 
None

extend(*other*)[](#pikepdf._core.PageList.extend)
: 
Extend the `Pdf` by adding pages from an iterable of pages.

While this method copies pages from one document to another, it does not
copy certain metadata such as annotations, form fields, bookmarks or
structural tree elements. Copying these is a more complex, application
specific operation.

**Parameters:**

**other** ([*PageList*](#pikepdf._core.PageList)* | **collections.abc.Iterable**[*[*Page*](models.html#pikepdf.Page)*]*)

**Return type:**
: 
None

from_objgen(*objgen: tuple[int, int]*) &#x2192; [Page](models.html#pikepdf.Page)[](#pikepdf._core.PageList.from_objgen)
: 
Given an objgen (object ID, generation), return the page.

Raises an exception if no page matches.

index(*page*)[](#pikepdf._core.PageList.index)
: 
Given a page, find the index.

That is, returns `n` such that `pdf.pages[n] == this_page`.
A `ValueError` exception is thrown if the page does not belong to
to this `Pdf`. The first page has index 0.

**Parameters:**

**page** ([*Page*](models.html#pikepdf.Page))

**Return type:**
: 
int

insert(*index*, *obj*)[](#pikepdf._core.PageList.insert)
: 
Insert a page at the specified location.

**Parameters:**

- 
**index** (*int*) – location at which to insert page, 0-based indexing

- 
**obj** ([*Page*](models.html#pikepdf.Page)) – page object to insert

**Return type:**
: 
None

p(*pnum*)[](#pikepdf._core.PageList.p)
: 
Look up page number in ordinal numbering, where 1 is the first page.

This is provided for convenience in situations where ordinal numbering
is more natural. It is equivalent to `.pages[pnum - 1]`. `.p(0)`
is an error and negative indexing is not supported.

If the PDF defines custom page labels (such as labeling front matter
with Roman numerals and the main body with Arabic numerals), this
function does not account for that. Use [`pikepdf.Page.label`](models.html#pikepdf.Page.label)
to get the page label for a page.

**Parameters:**

**pnum** (*int*)

**Return type:**
: 
[Page](models.html#pikepdf.Page)

remove(*page=None*, ***, *p*)[](#pikepdf._core.PageList.remove)
: 
Remove a page.

**Parameters:**

- 
**page** ([*Page*](models.html#pikepdf.Page)* | **None*) – If page is not None, remove that page.

- 
**p** (*int*) – 1-based page number to remove, if page is None.

**Return type:**
: 
None

reverse()[](#pikepdf._core.PageList.reverse)
: 
Reverse the order of pages.

**Return type:**

None

*class *pikepdf._core._ObjectList[](#pikepdf._core._ObjectList)
: 
A list whose elements are always pikepdf.Object.

In all other respects, this object behaves like a standard Python
list.

append(*x*)[](#pikepdf._core._ObjectList.append)

**Parameters:**

**x** ([*Object*](#pikepdf.Object))

**Return type:**
: 
None

clear()[](#pikepdf._core._ObjectList.clear)
: 

**Return type:**

None

count(*x*)[](#pikepdf._core._ObjectList.count)
: 

**Parameters:**

**x** ([*Object*](#pikepdf.Object))

**Return type:**
: 
int

extend(*L: [_ObjectList](#pikepdf._core._ObjectList)*) &#x2192; None[](#pikepdf._core._ObjectList.extend)
: 

insert(*i*, *x*)[](#pikepdf._core._ObjectList.insert)
: 

**Parameters:**

- 
**i** (*int*)

- 
**x** ([*Object*](#pikepdf.Object))

**Return type:**
: 
None

pop() &#x2192; [Object](#pikepdf.Object)[](#pikepdf._core._ObjectList.pop)
: 

remove(*x*)[](#pikepdf._core._ObjectList.remove)
: 

**Parameters:**

**x** ([*Object*](#pikepdf.Object))

**Return type:**
: 
None

*class *pikepdf.ObjectType(**args*, ***kwds*)[](#pikepdf.ObjectType)
: 
Enumeration of PDF object types.

These values are used to implement
pikepdf’s instance type checking. In the vast majority of cases it is more
pythonic to use `isinstance(obj, pikepdf.Stream)` or `issubclass`.

These values are low-level and documented for completeness. They are exposed
through `pikepdf.Object._type_code`.

array*: int** = Ellipsis*[](#pikepdf.ObjectType.array)

A PDF array, meaning the object is a `pikepdf.Array`.

boolean*: int** = Ellipsis*[](#pikepdf.ObjectType.boolean)
: 
A PDF boolean. In most cases, booleans are automatically converted to
`bool`, so this should not appear.

dictionary*: int** = Ellipsis*[](#pikepdf.ObjectType.dictionary)
: 
A PDF dictionary, meaning the object is a `pikepdf.Dictionary`.

inlineimage*: int** = Ellipsis*[](#pikepdf.ObjectType.inlineimage)
: 
A PDF inline image, meaning the object is the data stream of an inline
image. It would be necessary to combine this with the implicit
dictionary to interpret the image correctly. pikepdf automatically
packages inline images into a more useful class, so this will not
generally appear.

integer*: int** = Ellipsis*[](#pikepdf.ObjectType.integer)
: 
A PDF integer. In most cases, integers are automatically converted to
`int`, so this should not appear. Unlike Python integers, PDF integers
are 32-bit signed integers.

name_*: int** = Ellipsis*[](#pikepdf.ObjectType.name_)
: 
A PDF name, meaning the object is a `pikepdf.Name`.

null*: int** = Ellipsis*[](#pikepdf.ObjectType.null)
: 
A PDF null. In most cases, nulls are automatically converted to `None`,
so this should not appear.

operator*: int** = Ellipsis*[](#pikepdf.ObjectType.operator)
: 
A PDF operator, meaning the object is a `pikepdf.Operator`.

real*: int** = Ellipsis*[](#pikepdf.ObjectType.real)
: 
A PDF real. In most cases, reals are automatically convert to
`decimal.Decimal`.

reserved*: int** = Ellipsis*[](#pikepdf.ObjectType.reserved)
: 
A temporary object used in creating circular references. Should not appear
in most cases.

stream*: int** = Ellipsis*[](#pikepdf.ObjectType.stream)
: 
A PDF stream, meaning the object is a `pikepdf.Stream` (and it also
has a dictionary).

string*: int** = Ellipsis*[](#pikepdf.ObjectType.string)
: 
A PDF string, meaning the object is a `pikepdf.String`.

uninitialized*: int** = Ellipsis*[](#pikepdf.ObjectType.uninitialized)
: 
An uninitialized object. If this appears, it is probably a bug.

## Jobs[](#jobs)

*class *pikepdf.Job(*json: str*)[](#pikepdf.Job)
: 
Provides access to the qpdf job interface.

All of the functionality of the `qpdf` command line program
is now available to pikepdf through jobs.

**For further details:**
[https://qpdf.readthedocs.io/en/stable/qpdf-job.html](https://qpdf.readthedocs.io/en/stable/qpdf-job.html)

EXIT_CORRECT_PASSWORD*: ClassVar[int]** = 3*[](#pikepdf.Job.EXIT_CORRECT_PASSWORD)
: 

EXIT_ERROR*: ClassVar[int]** = 2*[](#pikepdf.Job.EXIT_ERROR)
: 
Exit code for a job that had an error.

EXIT_IS_NOT_ENCRYPTED*: ClassVar[int]** = 2*[](#pikepdf.Job.EXIT_IS_NOT_ENCRYPTED)
: 
Exit code for a job that provide a password when the input was not encrypted.

EXIT_WARNING*: ClassVar[int]** = 3*[](#pikepdf.Job.EXIT_WARNING)
: 
Exit code for a job that had a warning.

LATEST_JOB_JSON*: ClassVar[int]*[](#pikepdf.Job.LATEST_JOB_JSON)
: 
Version number of the most recent job-JSON schema.

LATEST_JSON*: ClassVar[int]*[](#pikepdf.Job.LATEST_JSON)
: 
Version number of the most recent qpdf-JSON schema.

__init__(*json: str*) &#x2192; None[](#pikepdf.Job.__init__)
: 
Create a Job from command line arguments to the qpdf program.

The first item in the `args` list should be equal to `progname`,
whose default is `&quot;pikepdf&quot;`.

Example

job = Job([‘pikepdf’, ‘–check’, ‘input.pdf’])
job.run()

check_configuration()[](#pikepdf.Job.check_configuration)
: 
Checks if the configuration is valid; raises an exception if not.

**Return type:**

None

create_pdf()[](#pikepdf.Job.create_pdf)
: 
Executes the first stage of the job.

*property *creates_output*: bool*[](#pikepdf.Job.creates_output)
: 
Returns True if the Job will create some sort of output file.

**Return type:**

bool

*property *encryption_status*: dict[str, bool]*[](#pikepdf.Job.encryption_status)
: 
Returns a Python dictionary describing the encryption status.

**Return type:**

dict[str, bool]

*property *exit_code*: int*[](#pikepdf.Job.exit_code)
: 
After run(), returns an integer exit code.

The meaning of exit code depends on the details of the Job that was run.
Details are subject to change in libqpdf. Use properties `has_warnings`
and `encryption_status` instead.

**Return type:**

int

*property *has_warnings*: bool*[](#pikepdf.Job.has_warnings)
: 
After run(), returns True if there were warnings.

**Return type:**

bool

*static *job_json_schema(***, *schema*)[](#pikepdf.Job.job_json_schema)
: 
For reference, the qpdf job command line schema is built-in.

**Parameters:**

**schema** (*int*)

**Return type:**
: 
str

*static *json_out_schema(***, *schema*)[](#pikepdf.Job.json_out_schema)
: 
For reference, the qpdf JSON output schema is built-in.

**Parameters:**

**schema** (*int*)

**Return type:**
: 
str

*property *message_prefix*: str*[](#pikepdf.Job.message_prefix)
: 
Allows manipulation of the prefix in front of all output messages.

**Return type:**

str

run()[](#pikepdf.Job.run)
: 
Executes the job.

**Return type:**

None

write_pdf(*pdf*)[](#pikepdf.Job.write_pdf)
: 
Executes the second stage of the job.

**Parameters:**

**pdf** ([*Pdf*](#pikepdf.Pdf))

---
# Tutorial
Source: https://pikepdf.readthedocs.io/en/latest/tutorial.html

# Tutorial[](#tutorial)

This brief tutorial should give you an introduction and orientation to pikepdf’s
paradigm and syntax. From there, we refer to you various topics.

## Opening and saving PDFs[](#opening-and-saving-pdfs)

In contrast to better known PDF libraries, pikepdf uses a single object to
represent a PDF, whether reading, writing or merging. We have cleverly named
this [`pikepdf.Pdf`](api/main.html#pikepdf.Pdf). In this documentation, a `Pdf` is a class that
allows manipulating the PDF, meaning the “file” (whether it exists in memory or on
a file system).

```
from pikepdf import Pdf

with Pdf.open(&#39;sample.pdf&#39;) as pdf:
    pdf.save(&#39;output.pdf&#39;)

```

You may of course use `from pikepdf import Pdf as ...` if the short class
name conflicts or `from pikepdf import Pdf as PDF` if you prefer uppercase.

[`pikepdf.open()`](api/main.html#pikepdf.open) is a shorthand for [`pikepdf.Pdf.open()`](api/main.html#pikepdf.Pdf.open).

The PDF class API follows the example of the widely-used
[Pillow image library](https://pillow.readthedocs.io/en/latest/). For clarity
there is no default constructor since the arguments used for creation and
opening are different. To make a new empty PDF, use `Pdf.new()` not `Pdf()`.

`Pdf.open()` also accepts seekable streams as input, and [`pikepdf.Pdf.save()`](api/main.html#pikepdf.Pdf.save) accepts
streams as output. `pathlib.Path` objects are fully supported wherever
pikepdf accepts a filename.

## Creating PDFs[](#creating-pdfs)

Using [`pikepdf.Pdf.new()`](api/main.html#pikepdf.Pdf.new), you can create a new PDF from scratch. pikepdf
is not primarily a PDF generation library - you may find other libraries easier
to use for that purpose. However, pikepdf does provide a few useful functions
for creating PDFs.

```
from pikepdf import Pdf

pdf = Pdf.new()
pdf.add_blank_page()
pdf.save(&#39;blank_page.pdf&#39;)

```

---
# Pages
Source: https://pikepdf.readthedocs.io/en/latest/topics/pages.html

# PDF split, merge, and document assembly[](#pdf-split-merge-and-document-assembly)

This section discusses working with PDF pages: splitting, merging, copying,
deleting. We’re treating pages as a unit, rather than working with the content of
individual pages.

Let’s continue with `fourpages.pdf` from the [Tutorial](../tutorial.html#tutorial).

```
&gt;&gt;&gt; from pikepdf import Pdf

&gt;&gt;&gt; pdf = Pdf.open(&#39;../tests/resources/fourpages.pdf&#39;)

```

Note

In some parts of the documentation we skip closing `Pdf` objects for brevity.
In production code, you should open them in a `with` block or explicitly
close them.

## Split a PDF into single page PDFs[](#split-a-pdf-into-single-page-pdfs)

All we need are new PDFs to hold the destination pages.

```
&gt;&gt;&gt; pdf = Pdf.open(&#39;../tests/resources/fourpages.pdf&#39;)

&gt;&gt;&gt; for n, page in enumerate(pdf.pages):
...     dst = Pdf.new()
...     dst.pages.append(page)
...     dst.save(f&#39;{n:02d}.pdf&#39;)

```

Note

This example will transfer data associated with each page, so
that every page stands on its own. It will *not* transfer some metadata
associated with the PDF as a whole, such as the list of bookmarks.

---
# Attachments
Source: https://pikepdf.readthedocs.io/en/latest/topics/attachments.html

# Attaching files to a PDF[](#attaching-files-to-a-pdf)

Added in version 3.0.

You can attach (or if you prefer, embed) any file to a PDF, including
other PDFs. As a quick example, let’s attach pikepdf’s README.md file
to one of its test files.

```
&gt;&gt;&gt; from pikepdf import Pdf, AttachedFileSpec, Name, Dictionary, Array

&gt;&gt;&gt; from pathlib import Path

&gt;&gt;&gt; pdf = Pdf.open(&#39;../tests/resources/fourpages.pdf&#39;)

&gt;&gt;&gt; filespec = AttachedFileSpec.from_filepath(pdf, Path(&#39;../README.md&#39;))

&gt;&gt;&gt; pdf.attachments[&#39;README.md&#39;] = filespec

&gt;&gt;&gt; pdf.attachments
&lt;pikepdf._core.Attachments: [&#39;README.md&#39;]&gt;

```

This creates an attached file named `README.md`, which holds the data in `filespec`.
Now we can retrieve the data.

```
&gt;&gt;&gt; pdf.attachments[&#39;README.md&#39;]
&lt;pikepdf._core.AttachedFileSpec for &#39;README.md&#39;, description &#39;&#39;&gt;

&gt;&gt;&gt; file = pdf.attachments[&#39;README.md&#39;].get_file()

```

```
&gt;&gt;&gt; file.read_bytes()[...]
b&#39;**pikepdf** is a Python library for reading and writing PDF files.&#39;

```

If the data used to create an attachment is in memory:

```
&gt;&gt;&gt; memfilespec = AttachedFileSpec(pdf, b&#39;Some text&#39;, mime_type=&#39;text/plain&#39;)

&gt;&gt;&gt; pdf.attachments[&#39;plain.txt&#39;] = memfilespec

```

## General notes on attached files[](#general-notes-on-attached-files)

- 
If the main PDF is encrypted, any embedded files will be encrypted with the same
encryption settings.

- 
PDF viewers tend to display attachment filenames in alphabetical order. Use prefixes
if you want to control the display order.

- 
The `AttachedFileSpec` will capture all of the data when created, so the file object
used to create the data can be closed.

- 
Each attachment is a [`pikepdf.AttachedFileSpec`](../api/models.html#pikepdf.AttachedFileSpec). An attachment usually contains only
one `pikepdf.AttachedFile`, but might contain multiple objects of this
type. Usually, multiple versions are used to provide different versions of the
same file for alternate platforms, such as Windows and macOS versions of a file.
Newer PDFs rarely provide multiple versions.

## How to find attachments in a PDF viewer[](#how-to-find-attachments-in-a-pdf-viewer)

Your PDF viewer should have an attachments panel that shows available attachments.

Attachments in Adobe Acrobat DC.[](#id1)

Attachments added to `Pdf.attachments` will be shown here.

You may find it useful to set `pdf.root.PageMode = Name.UseAttachments`. This
tells the PDF viewer to open a pane that lists all attachments in the PDF. Note
that it is up to the PDF viewer to implement and honor this request.

## Creating attachment annotations[](#creating-attachment-annotations)

You can also create PDF Annotations and Actions that contain attached files.

Here is an example of an annotation that displays an icon. Clicking the icon
prompt the user to view the attached document.

```
&gt;&gt;&gt; pdf = Pdf.open(&#39;../tests/resources/fourpages.pdf&#39;)

&gt;&gt;&gt; filespec = AttachedFileSpec.from_filepath(pdf, Path(&#39;../README.md&#39;))

&gt;&gt;&gt; pushpin = Dictionary(
...     Type=Name.Annot,
...     Subtype=Name.FileAttachment,
...     Name=Name.GraphPushPin,
...     FS=filespec.obj,
...     Rect=[2*72, 9*72, 3*72, 10*72],
... )

&gt;&gt;&gt; pdf.pages[0].Annots = pdf.make_indirect(Array([
...     pushpin
... ]))

```

Files that are referenced as Annotations and Actions do not need to be added
to `Pdf.attachments`. If they are, the file will be attached twice.

---
# Security
Source: https://pikepdf.readthedocs.io/en/latest/topics/security.html

# PDF security[](#pdf-security)

## Password security[](#password-security)

Password security in PDFs is widely supported, including by pikepdf. Unfortunately,
its security has limitations and may offer more security theatre than real
security, depending on your needs.

Note the following limitations of password security in PDFs:

- 
anyone with the user password *or* the owner password can open the PDF, extract
its contents, and produce a visually identical PDF;

- 
if the user password is an empty string, everyone has the user password;

- 
setting a user password and leaving the owner password blank is useless;

- 
the only thing you can not do if you have the user password and not the owner
password is create a new PDF encrypted with the same owner password;

- 
`pikepdf.Permissions` restrictions depend entirely on the PDF viewer software
to enforce the restrictions – libraries like pikepdf can bypass those restrictions;

- 
cracking PDF passwords is easier than many other forms of cracking because
a motivated person has unlimited chances to guess the password on a static file.

While the AES encryption algorithm is strong, password-protected PDFs have
significant practical weaknesses.

In view of all of this, the most useful option is to set the owner password to a
strong password, and the user password to blank. This allows anyone to view the PDF
while allowing you to prove that you (or your software’s user) generated the PDF by
producing the strong owner password.

### Unicode in passwords[](#unicode-in-passwords)

For widest compatibility, passwords should be composed of only characters in the
ASCII character set, since the [PDF 1.7 Reference Manual](../references/resources.html) is unclear about how non-ASCII
passwords are supposed to be encoded. See the documentation on [`pikepdf.Pdf.save()`](../api/main.html#pikepdf.Pdf.save)
for more details. pikepdf encodes passwords as UTF-8.

## PDF content restrictions[](#pdf-content-restrictions)

If you are developing a PDF application, you should enforce the restrictions in
[`pikepdf.Permissions`](../api/models.html#pikepdf.Permissions), and not permit people who have only the user password
to access restricted content. If the PDF is opened with the owner password,
any content may be accessed without enforcing restrictions.
[`pikepdf.Pdf.user_password_matched`](../api/main.html#pikepdf.Pdf.user_password_matched) and [`pikepdf.Pdf.owner_password_matched`](../api/main.html#pikepdf.Pdf.owner_password_matched)
can be used to check which password opened the PDF.

It is up to the application developer to implement the restrictions. pikepdf or
any PDF manipulation library can be used to bypass restrictions.

## Digital signatures and certificates[](#digital-signatures-and-certificates)

PDFs signed with a digital signature can mitigate some of these security issues.
pikepdf does not support digital signatures at this time.

---
# Outlines
Source: https://pikepdf.readthedocs.io/en/latest/topics/outlines.html

# Outlines[](#outlines)

Outlines (sometimes also called *bookmarks*) are shown in a the PDF viewer
aside of the page, allowing for navigation within the document.

## Creating outlines[](#creating-outlines)

Outlines can be created from scratch, e.g. when assembling a set of PDF files
into a single document.

The following example adds outline entries referring to the 1st, 3rd and 9th page
of an existing PDF.

```
&gt;&gt;&gt; from pikepdf import Pdf, OutlineItem

&gt;&gt;&gt; pdf = Pdf.open(&#39;document.pdf&#39;)

&gt;&gt;&gt; with pdf.open_outline() as outline:
...     outline.root.extend([
...         # Page counts are zero-based
...         OutlineItem(&#39;Section One&#39;, 0),
...         OutlineItem(&#39;Section Two&#39;, 2),
...         OutlineItem(&#39;Section Three&#39;, 8)
...     ])

&gt;&gt;&gt; pdf.save(&#39;document_with_outline.pdf&#39;)

```

Another example, for automatically adding an entry for each file in a merged document:

```
&gt;&gt;&gt; from glob import glob

&gt;&gt;&gt; pdf = Pdf.new()

&gt;&gt;&gt; page_count = 0

&gt;&gt;&gt; with pdf.open_outline() as outline:
...     for file in glob(&#39;*.pdf&#39;):
...         src = Pdf.open(file)
...         oi = OutlineItem(file, page_count)
...         outline.root.append(oi)
...         page_count += len(src.pages)
...         pdf.pages.extend(src.pages)

&gt;&gt;&gt; pdf.save(&#39;merged.pdf&#39;)

```

---
# Models
Source: https://pikepdf.readthedocs.io/en/latest/api/models.html

# Support models[](#support-models)

Support models are abstracts over “raw” objects within a Pdf. For example, a page
in a PDF is a Dictionary with set to `/Type` of `/Page`. The Dictionary in
that case is the “raw” object. Upon establishing what type of object it is, we
can wrap it with a support model that adds features to ensure consistency with
the PDF specification.

In version 2.x, did not apply support models to “raw” objects automatically.
Version 3.x automatically applies support models to `/Page` objects.

*class *pikepdf.ObjectHelper[](#pikepdf.ObjectHelper)
: 
Base class for wrapper/helper around an Object.

Used to expose additional functionality specific to that object type.

[`pikepdf.Page`](#pikepdf.Page) is an example of an object helper. The actual
page object is a PDF is a Dictionary. The helper provides additional
methods specific to pages.

*property *obj*: pikepdf.objects.Dictionary*[](#pikepdf.ObjectHelper.obj)

Get the underlying PDF object (typically a Dictionary).

**Return type:**

pikepdf.objects.Dictionary

*class *pikepdf.Page(*arg0: [Object](main.html#pikepdf.Object)*)[](#pikepdf.Page)
: 
Support model wrapper around a page dictionary object.

add_content_token_filter(*tf*)[](#pikepdf.Page.add_content_token_filter)

Attach a [`pikepdf.TokenFilter`](filters.html#pikepdf.TokenFilter) to a page’s content stream.

This function applies token filters lazily, if/when the page’s
content stream is read for any reason, such as when the PDF is
saved. If never access, the token filter is not applied.

Multiple token filters may be added to a page/content stream.

Token filters may not be removed after being attached to a Pdf.
Close and reopen the Pdf to remove token filters.

If the page’s contents is an array of streams, it is coalesced.

**Parameters:**

**tf** ([*TokenFilter*](filters.html#pikepdf.TokenFilter)) – The token filter to attach.

**Return type:**
: 
None

add_overlay(*other*, *rect*, ***, *push_stack=...*)[](#pikepdf.Page.add_overlay)
: 
Overlay another object on this page.

Overlays will be drawn after all previous content, potentially drawing on top
of existing content.

**Parameters:**

- 
**other** ([*Object*](main.html#pikepdf.Object)* | *[*Page*](#pikepdf.Page)) – A Page or Form XObject to render as an overlay on top of this
page.

- 
**rect** ([*Rectangle*](main.html#pikepdf.Rectangle)* | **None*) – The PDF rectangle (in PDF units) in which to draw the overlay.
If omitted, this page’s trimbox, cropbox or mediabox (in that order)
will be used.

- 
**push_stack** (*bool** | **None*) – If True (default), push the graphics stack of the existing
content stream to ensure that the overlay is rendered correctly.
Officially PDF limits the graphics stack depth to 32. Most
viewers will tolerate more, but excessive pushes may cause problems.
Multiple content streams may also be coalesced into a single content
stream where this parameter is True, since the PDF specification
permits PDF writers to coalesce streams as they see fit.

- 
**shrink** – If True (default), allow the object to shrink to fit inside the
rectangle. The aspect ratio will be preserved.

- 
**expand** – If True (default), allow the object to expand to fit inside the
rectangle. The aspect ratio will be preserved.

**Returns:**
: 
The name of the Form XObject that contains the overlay.

Added in version 2.14.

Changed in version 4.0.0: Added the *push_stack* parameter. Previously, this method behaved
as if *push_stack* were False.

Changed in version 4.2.0: Added the *shrink* and *expand* parameters. Previously, this method
behaved as if `shrink=True, expand=False`.

Changed in version 4.3.0: Returns the name of the overlay in the resources dictionary instead
of returning None.

add_resource(*res*, *res_type*, *name=None*, ***, *prefix=''*, *replace_existing=True*)[](#pikepdf.Page.add_resource)
: 
Add a new resource to the page’s Resources dictionary.

If the Resources dictionaries do not exist, they will be created.

**Parameters:**

- 
**self** – The object to add to the resources dictionary.

- 
**res** ([*Object*](main.html#pikepdf.Object)) – The dictionary object to insert into the resources
dictionary.

- 
**res_type** (*pikepdf.objects.Name*) – Should be one of the following Resource dictionary types:
ExtGState, ColorSpace, Pattern, Shading, XObject, Font, Properties.

- 
**name** (*pikepdf.objects.Name** | **None*) – The name of the object. If omitted, a random name will be
generated with enough randomness to be globally unique.

- 
**prefix** (*str*) – A prefix for the name of the object. Allows conveniently
namespacing when using random names, e.g. prefix=”Im” for images.
Mutually exclusive with name parameter.

- 
**replace_existing** (*bool*) – If the name already exists in one of the resource
dictionaries, remove it.

**Return type:**
: 
pikepdf.objects.Name

Example

```
&gt;&gt;&gt; pdf = pikepdf.Pdf.new()
&gt;&gt;&gt; pdf.add_blank_page(page_size=(100, 100))
&lt;pikepdf.Page({
  &quot;/Contents&quot;: pikepdf.Stream(owner=&lt;...&gt;, data=&lt;...&gt;, {

  }),
  &quot;/MediaBox&quot;: [ 0, 0, 100, 100 ],
  &quot;/Parent&quot;: &lt;reference to /Pages&gt;,
  &quot;/Resources&quot;: {

  },
  &quot;/Type&quot;: &quot;/Page&quot;
})&gt;
&gt;&gt;&gt; formxobj = pikepdf.Dictionary(
...     Type=Name.XObject,
...     Subtype=Name.Form
... )
&gt;&gt;&gt; resource_name = pdf.pages[0].add_resource(formxobj, Name.XObject)

```

Added in version 2.3.

Changed in version 2.14: If *res* does not belong to the same Pdf that owns this page,
a copy of *res* is automatically created and added instead. In previous
versions, it was necessary to change for this case manually.

Changed in version 4.3.0: Returns the name of the overlay in the resources dictionary instead
of returning None.

add_underlay(*other*, *rect*)[](#pikepdf.Page.add_underlay)
: 
Underlay another object beneath this page.

Underlays will be drawn before all other content, so they may be overdrawn
partially or completely.

There is no *push_stack* parameter for this function, since adding an
underlay can be done without manipulating the graphics stack.

**Parameters:**

- 
**other** ([*Object*](main.html#pikepdf.Object)* | *[*Page*](#pikepdf.Page)) – A Page or Form XObject to render as an underlay underneath this
page.

- 
**rect** ([*Rectangle*](main.html#pikepdf.Rectangle)* | **None*) – The PDF rectangle (in PDF units) in which to draw the underlay.
If omitted, this page’s trimbox, cropbox or mediabox (in that order)
will be used.

- 
**shrink** – If True (default), allow the object to shrink to fit inside the
rectangle. The aspect ratio will be preserved.

- 
**expand** – If True (default), allow the object to expand to fit inside the
rectangle. The aspect ratio will be preserved.

**Returns:**
: 
The name of the Form XObject that contains the underlay.

Added in version 2.14.

Changed in version 4.2.0: Added the *shrink* and *expand* parameters. Previously, this method
behaved as if `shrink=True, expand=False`. Fixed issue with wrong
page rect being selected.

*property *artbox*: pikepdf.objects.Array*[](#pikepdf.Page.artbox)
: 
Return page’s effective /ArtBox, in PDF units.

According to the PDF specification:
“The art box defines the page’s meaningful content area, including
white space.”

If the /ArtBox is not defined, the /CropBox is returned.

**Return type:**

pikepdf.objects.Array

as_form_xobject(*handle_transformations=...*)[](#pikepdf.Page.as_form_xobject)
: 
Return a form XObject that draws this page.

This is useful for
n-up operations, underlay, overlay, thumbnail generation, or
any other case in which it is useful to replicate the contents
of a page in some other context. The dictionaries are shallow
copies of the original page dictionary, and the contents are
coalesced from the page’s contents. The resulting object handle
is not referenced anywhere.

**Parameters:**

**handle_transformations** (*bool*) – If True (default), the resulting form
XObject’s `/Matrix` will be set to replicate rotation
(`/Rotate`) and scaling (`/UserUnit`) in the page’s
dictionary. In this way, the page’s transformations will
be preserved when placing this object on another page.

**Return type:**
: 
[Object](main.html#pikepdf.Object)

*property *bleedbox*: pikepdf.objects.Array*[](#pikepdf.Page.bleedbox)
: 
Return page’s effective /BleedBox, in PDF units.

According to the PDF specification:
“The bleed box defines the region to which the contents of the page
should be clipped when output in a print production environment.”

If the /BleedBox is not defined, the /CropBox is returned.

**Return type:**

pikepdf.objects.Array

calc_form_xobject_placement(*formx*, *name*, *rect*, ***, *invert_transformations*, *allow_shrink*, *allow_expand*)[](#pikepdf.Page.calc_form_xobject_placement)
: 
Generate content stream segment to place a Form XObject on this page.

The content stream segment must then be added to the page’s
content stream.

The default keyword parameters will preserve the aspect ratio.

**Parameters:**

- 
**formx** ([*Object*](main.html#pikepdf.Object)) – The Form XObject to place.

- 
**name** (*pikepdf.objects.Name*) – The name of the Form XObject in this page’s /Resources
dictionary.

- 
**rect** ([*Rectangle*](main.html#pikepdf.Rectangle)) – Rectangle describing the desired placement of the Form
XObject.

- 
**invert_transformations** (*bool*) – Apply /Rotate and /UserUnit scaling
when determining FormX Object placement.

- 
**allow_shrink** (*bool*) – Allow the Form XObject to take less than the
full dimensions of rect.

- 
**allow_expand** (*bool*) – Expand the Form XObject to occupy all of rect.

**Return type:**
: 
bytes

Added in version 2.14.

contents_add(*contents*, ***, *prepend=...*)[](#pikepdf.Page.contents_add)
: 
Append or prepend to an existing page’s content stream.

**Parameters:**

- 
**contents** (*pikepdf.objects.Stream** | **bytes*) – An existing content stream to append or prepend.

- 
**prepend** (*bool*) – Prepend if true, append if false (default).

**Return type:**
: 
None

Added in version 2.14.

contents_coalesce()[](#pikepdf.Page.contents_coalesce)
: 
Coalesce a page’s content streams.

A page’s content may be a
stream or an array of streams. If this page’s content is an
array, concatenate the streams into a single stream. This can
be useful when working with files that split content streams in
arbitrary spots, such as in the middle of a token, as that can
confuse some software.

**Return type:**

None

*property *cropbox*: pikepdf.objects.Array*[](#pikepdf.Page.cropbox)
: 
Return page’s effective /CropBox, in PDF units.

According to the PDF specification:
“The crop box defines the region to which the contents of the page
shall be clipped (cropped) when displayed or printed. It has no
defined meaning in the context of the PDF imaging model; it merely
imposes clipping on the page contents.”

If the /CropBox is not defined, the /MediaBox is returned.

**Return type:**

pikepdf.objects.Array

emplace(*other*, *retain=...*)[](#pikepdf.Page.emplace)
: 

**Parameters:**

- 
**other** ([*Page*](#pikepdf.Page))

- 
**retain** (*collections.abc.Iterable**[**pikepdf.objects.Name**]*)

**Return type:**
: 
None

externalize_inline_images(*min_size=...*, *shallow=...*)[](#pikepdf.Page.externalize_inline_images)
: 
Convert inline image to normal (external) images.

**Parameters:**

- 
**min_size** (*int*) – minimum size in bytes

- 
**shallow** (*bool*) – If False, recurse into nested Form XObjects.
If True, do not recurse.

**Return type:**
: 
None

form_xobjects()[](#pikepdf.Page.form_xobjects)
: 
Return all Form XObjects associated with this page.

This method does not recurse into nested Form XObjects.

Added in version 7.0.0.

**Return type:**

_ObjectMapping

get(*key*, *default=...*)[](#pikepdf.Page.get)
: 

**Parameters:**

- 
**key** (*str** | **pikepdf.objects.Name*)

- 
**default** (*T** | **None*)

**Return type:**
: 
T | None | [Object](main.html#pikepdf.Object)

get_filtered_contents(*tf*)[](#pikepdf.Page.get_filtered_contents)
: 
Apply a [`pikepdf.TokenFilter`](filters.html#pikepdf.TokenFilter) to a content stream.

This may be used when the results of a token filter do not need
to be applied, such as when filtering is being used to retrieve
information rather than edit the content stream.

Note that it is possible to create a subclassed `TokenFilter`
that saves information of interest to its object attributes; it
is not necessary to return data in the content stream.

To modify the content stream, use [`pikepdf.Page.add_content_token_filter()`](#pikepdf.Page.add_content_token_filter).

**Returns:**

The result of modifying the content stream with `tf`.
The existing content stream is not modified.

**Parameters:**
: 
**tf** ([*TokenFilter*](filters.html#pikepdf.TokenFilter))

**Return type:**
: 
bytes

*property *images*: _ObjectMapping*[](#pikepdf.Page.images)
: 
Return all regular images associated with this page.

This method does not search for Form XObjects that contain images,
and does not attempt to find inline images.

**Return type:**

_ObjectMapping

index()[](#pikepdf.Page.index)
: 
Returns the zero-based index of this page in the pages list.

That is, returns `n` such that `pdf.pages[n] == this_page`.
A `ValueError` exception is thrown if the page is not attached
to this `Pdf`.

Added in version 2.2.

**Return type:**

int

label()[](#pikepdf.Page.label)
: 
Returns the page label for this page, accounting for section numbers.

For example, if the PDF defines a preface with lower case Roman
numerals (i, ii, iii…), followed by standard numbers, followed
by an appendix (A-1, A-2, …), this function returns the appropriate
label as a string.

It is possible for a PDF to define page labels such that multiple
pages have the same labels. Labels are not guaranteed to
be unique.

Added in version 2.2.

Changed in version 2.9: Returns the ordinary page number if no special rules for page
numbers are defined.

**Return type:**

str

*property *mediabox*: pikepdf.objects.Array*[](#pikepdf.Page.mediabox)
: 
Return page’s /MediaBox, in PDF units.

According to the PDF specification:
“The media box defines the boundaries of the physical medium on which
the page is to be printed.”

**Return type:**

pikepdf.objects.Array

*property *obj*: pikepdf.objects.Dictionary*[](#pikepdf.Page.obj)
: 

**Return type:**

pikepdf.objects.Dictionary

parse_contents(*stream_parser*)[](#pikepdf.Page.parse_contents)
: 
Parse a page’s content streams using a `pikepdf.StreamParser`.

The content stream may be interpreted by the StreamParser but is
not altered.

If the page’s contents is an array of streams, it is coalesced.

**Parameters:**

**stream_parser** (*StreamParser*) – A `pikepdf.StreamParser` instance.

**Return type:**
: 
None

remove_unreferenced_resources()[](#pikepdf.Page.remove_unreferenced_resources)
: 
Removes resources not referenced by content stream.

A page’s resources (`page.resources`) dictionary maps names to objects.
This method walks through a page’s contents and
keeps tracks of which resources are referenced somewhere in the
contents. Then it removes from the resources dictionary any
object that is not referenced in the contents. This
method is used by page splitting code to avoid copying unused
objects in files that use shared resource dictionaries across
multiple pages.

**Return type:**

None

*property *resources*: pikepdf.objects.Dictionary*[](#pikepdf.Page.resources)
: 
Return this page’s resources dictionary.

Changed in version 7.0.0: If the resources dictionary does not exist, an empty one will be created.
A TypeError is raised if a page has a /Resources key but it is not a
dictionary.

**Return type:**

pikepdf.objects.Dictionary

rotate(*angle*, *relative*)[](#pikepdf.Page.rotate)
: 
Rotate a page.

If `relative` is `False`, set the rotation of the
page to angle. Otherwise, add angle to the rotation of the
page. `angle` must be a multiple of `90`. Adding `90` to
the rotation rotates clockwise by `90` degrees.

**Parameters:**

- 
**angle** (*int*) – Rotation angle in degrees.

- 
**relative** (*bool*) – If `True`, add `angle` to the current
rotation. If `False`, set the rotation of the page
to `angle`.

**Return type:**
: 
None

*property *trimbox*: pikepdf.objects.Array*[](#pikepdf.Page.trimbox)
: 
Return page’s effective /TrimBox, in PDF units.

According to the PDF specification:
“The trim box defines the intended dimensions of the finished page
after trimming. It may be smaller than the media box to allow for
production-related content, such as printing instructions, cut marks,
or color bars.”

If the /TrimBox is not defined, the /CropBox is returned (and if
/CropBox is not defined, /MediaBox is returned).

**Return type:**

pikepdf.objects.Array

*class *pikepdf.PdfImage(*obj*)[](#pikepdf.PdfImage)
: 
Support class to provide a consistent API for manipulating PDF images.

The data structure for images inside PDFs is irregular and complex,
making it difficult to use without introducing errors for less
typical cases. This class addresses these difficulties by providing a
regular, Pythonic API similar in spirit (and convertible to) the Python
Pillow imaging library.

**Parameters:**

**obj** (*pikepdf.objects.Stream*)

MAIN_COLORSPACES[](#pikepdf.PdfImage.MAIN_COLORSPACES)
: 

PRINT_COLORSPACES[](#pikepdf.PdfImage.PRINT_COLORSPACES)
: 

SIMPLE_COLORSPACES[](#pikepdf.PdfImage.SIMPLE_COLORSPACES)
: 

as_pil_image()[](#pikepdf.PdfImage.as_pil_image)
: 
Extract the image as a Pillow Image, using decompression as necessary.

Caller must close the image.

**Return type:**

PIL.Image.Image

*property *bits_per_component*: int*[](#pikepdf.PdfImage.bits_per_component)
: 
Bits per component of this image.

**Return type:**

int

*property *colorspace*: str | None*[](#pikepdf.PdfImage.colorspace)
: 
PDF name of the colorspace that best describes this image.

**Return type:**

str | None

*property *decode_parms[](#pikepdf.PdfImage.decode_parms)
: 
List of the /DecodeParms, arguments to filters.

extract_to(***, *stream=None*, *fileprefix=''*)[](#pikepdf.PdfImage.extract_to)
: 
Extract the image directly to a usable image file.

If possible, the compressed data is extracted and inserted into
a compressed image file format without transcoding the compressed
content. If this is not possible, the data will be decompressed
and extracted to an appropriate format.

Because it is not known until attempted what image format will be
extracted, users should not assume what format they are getting back.
When saving the image to a file, use a temporary filename, and then
rename the file to its final name based on the returned file extension.

Images might be saved as any of .png, .jpg, or .tiff.

Examples

```
&gt;&gt;&gt; im.extract_to(stream=bytes_io)
&#39;.png&#39;

```

```
&gt;&gt;&gt; im.extract_to(fileprefix=&#39;/tmp/image00&#39;)
&#39;/tmp/image00.jpg&#39;

```

**Parameters:**

- 
**stream** (*BinaryIO** | **None*) – Writable stream to write data to.

- 
**fileprefix** (*str** or **Path*) – The path to write the extracted image to,
without the file extension.

**Returns:**
: 
If *fileprefix* was provided, then the fileprefix with the
appropriate extension. If no *fileprefix*, then an extension
indicating the file type.

**Return type:**
: 
str

*property *filter_decodeparms[](#pikepdf.PdfImage.filter_decodeparms)
: 
Return normalized the Filter and DecodeParms data.

PDF has a lot of possible data structures concerning /Filter and
/DecodeParms. /Filter can be absent or a name or an array, /DecodeParms
can be absent or a dictionary (if /Filter is a name) or an array (if
/Filter is an array). When both are arrays the lengths match.

Normalize this into:
[(/FilterName, {/DecodeParmName: Value, …}), …]

The order of /Filter matters as indicates the encoding/decoding sequence.

*property *filters[](#pikepdf.PdfImage.filters)
: 
List of names of the filters that we applied to encode this image.

get_stream_buffer(*decode_level=StreamDecodeLevel.specialized*)[](#pikepdf.PdfImage.get_stream_buffer)
: 
Access this image with the buffer protocol.

**Parameters:**

**decode_level** (*pikepdf._core.StreamDecodeLevel*)

**Return type:**
: 
pikepdf._core.Buffer

*property *height*: int*[](#pikepdf.PdfImage.height)
: 
Height of the image data in pixels.

**Return type:**

int

*property *icc*: PIL.ImageCms.ImageCmsProfile | None*[](#pikepdf.PdfImage.icc)
: 
If an ICC profile is attached, return a Pillow object that describe it.

Most of the information may be found in `icc.profile`.

**Return type:**

PIL.ImageCms.ImageCmsProfile | None

*property *image_mask*: bool*[](#pikepdf.PdfImage.image_mask)
: 
Return `True` if this is an image mask.

**Return type:**

bool

*property *indexed*: bool*[](#pikepdf.PdfImage.indexed)
: 
Check if the image has a defined color palette.

**Return type:**

bool

*property *is_device_n*: bool*[](#pikepdf.PdfImage.is_device_n)
: 
Check if image has a /DeviceN (complex printing) colorspace.

**Return type:**

bool

*property *is_separation*: bool*[](#pikepdf.PdfImage.is_separation)
: 
Check if image has a /DeviceN (complex printing) colorspace.

**Return type:**

bool

*property *mode*: str*[](#pikepdf.PdfImage.mode)
: 
`PIL.Image.mode` equivalent for this image, where possible.

If an ICC profile is attached to the image, we still attempt to resolve a Pillow
mode.

**Return type:**

str

obj*: pikepdf.objects.Stream*[](#pikepdf.PdfImage.obj)
: 

*property *palette*: PaletteData | None*[](#pikepdf.PdfImage.palette)
: 
Retrieve the color palette for this image if applicable.

**Return type:**

PaletteData | None

read_bytes(*decode_level=StreamDecodeLevel.specialized*)[](#pikepdf.PdfImage.read_bytes)
: 
Decompress this image and return it as unencoded bytes.

**Parameters:**

**decode_level** (*pikepdf._core.StreamDecodeLevel*)

**Return type:**
: 
bytes

show()[](#pikepdf.PdfImage.show)
: 
Show the image however PIL wants to.

*property *size*: tuple[int, int]*[](#pikepdf.PdfImage.size)
: 
Size of image as (width, height).

**Return type:**

tuple[int, int]

*property *width*: int*[](#pikepdf.PdfImage.width)
: 
Width of the image data in pixels.

**Return type:**

int

*class *pikepdf.PdfInlineImage(***, *image_data*, *image_object*)[](#pikepdf.PdfInlineImage)
: 
Support class for PDF inline images.

**Parameters:**

- 
**image_data** (*pikepdf.objects.Object*)

- 
**image_object** (*tuple*)

*class *pikepdf.models.PdfMetadata(*pdf*, *pikepdf_mark=True*, *sync_docinfo=True*, *overwrite_invalid_xml=True*)[](#pikepdf.models.PdfMetadata)
: 
Read and edit the metadata associated with a PDF.

The PDF specification contain two types of metadata, the newer XMP
(Extensible Metadata Platform, XML-based) and older DocumentInformation
dictionary. The PDF 2.0 specification removes the DocumentInformation
dictionary.

This primarily works with XMP metadata, but includes methods to generate
XMP from DocumentInformation and will also coordinate updates to
DocumentInformation so that the two are kept consistent.

XMP metadata fields may be accessed using the full XML namespace URI or
the short name. For example `metadata['dc:description']`
and `metadata['{http://purl.org/dc/elements/1.1/}description']`
both refer to the same field. Several common XML namespaces are registered
automatically.

See the XMP specification for details of allowable fields.

To update metadata, use a with block.

Example

```
&gt;&gt;&gt; with pdf.open_metadata() as records:
...     records[&#39;dc:title&#39;] = &#39;New Title&#39;

```

See also

[`pikepdf.Pdf.open_metadata()`](main.html#pikepdf.Pdf.open_metadata)

**Parameters:**

- 
**pdf** ([*pikepdf.Pdf*](main.html#pikepdf.Pdf))

- 
**pikepdf_mark** (*bool*)

- 
**sync_docinfo** (*bool*)

- 
**overwrite_invalid_xml** (*bool*)

DOCINFO_MAPPING*: list[DocinfoMapping]*[](#pikepdf.models.PdfMetadata.DOCINFO_MAPPING)
: 

NS*: dict[str, str]*[](#pikepdf.models.PdfMetadata.NS)
: 

REVERSE_NS*: dict[str, str]*[](#pikepdf.models.PdfMetadata.REVERSE_NS)
: 

load_from_docinfo(*docinfo*, *delete_missing=False*, *raise_failure=False*)[](#pikepdf.models.PdfMetadata.load_from_docinfo)
: 
Populate the XMP metadata object with DocumentInfo.

**Parameters:**

- 
**docinfo** – a DocumentInfo, e.g pdf.docinfo

- 
**delete_missing** (*bool*) – if the entry is not DocumentInfo, delete the equivalent
from XMP

- 
**raise_failure** (*bool*) – if True, raise any failure to convert docinfo;
otherwise warn and continue

**Return type:**
: 
None

A few entries in the deprecated DocumentInfo dictionary are considered
approximately equivalent to certain XMP records. This method copies
those entries into the XMP metadata.

mark* = True*[](#pikepdf.models.PdfMetadata.mark)
: 

overwrite_invalid_xml* = True*[](#pikepdf.models.PdfMetadata.overwrite_invalid_xml)
: 

*property *pdfa_status*: str*[](#pikepdf.models.PdfMetadata.pdfa_status)
: 
Return the PDF/A conformance level claimed by this PDF, or False.

A PDF may claim to PDF/A compliant without this being true. Use an
independent verifier such as veraPDF to test if a PDF is truly
conformant.

**Returns:**

The conformance level of the PDF/A, or an empty string if the
PDF does not claim PDF/A conformance. Possible valid values
are: 1A, 1B, 2A, 2B, 2U, 3A, 3B, 3U. Note that ISO standard
typically refers to PDF/A-1b for example, using lower case;
this function returns the value as it appears in the PDF, which
is uppercase.

**Return type:**
: 
str

*property *pdfx_status*: str*[](#pikepdf.models.PdfMetadata.pdfx_status)
: 
Return the PDF/X conformance level claimed by this PDF, or False.

A PDF may claim to PDF/X compliant without this being true. Use an
independent verifier such as veraPDF to test if a PDF is truly
conformant.

**Returns:**

The conformance level of the PDF/X, or an empty string if the
PDF does not claim PDF/X conformance.

**Return type:**
: 
str

*classmethod *register_xml_namespace(*uri*, *prefix*)[](#pikepdf.models.PdfMetadata.register_xml_namespace)
: 
Register a new XML/XMP namespace.

**Parameters:**

- 
**uri** – The long form of the namespace.

- 
**prefix** – The alias to use when interpreting XMP.

sync_docinfo* = True*[](#pikepdf.models.PdfMetadata.sync_docinfo)
: 

*class *pikepdf.models.Encryption[](#pikepdf.models.Encryption)
: 
Specify the encryption settings to apply when a PDF is saved.

R*: Literal[2, 3, 4, 5, 6]** = 6*[](#pikepdf.models.Encryption.R)

Select the security handler algorithm to use. Choose from:
`2`, `3`, `4` or `6`. By default, the highest version of
is selected (`6`). `5` is a deprecated algorithm that should
not be used.

aes*: bool** = True*[](#pikepdf.models.Encryption.aes)
: 
If True, request the AES algorithm. If False, use RC4.
If omitted, AES is selected whenever possible (R &gt;= 4).

allow*: [Permissions](#pikepdf.Permissions)*[](#pikepdf.models.Encryption.allow)
: 
The permissions to set.
If omitted, all permissions are granted to the user.

metadata*: bool** = True*[](#pikepdf.models.Encryption.metadata)
: 
If True, also encrypt the PDF metadata. If False,
metadata is not encrypted. Reading document metadata without
decryption may be desirable in some cases. Requires `aes=True`.
If omitted, metadata is encrypted whenever possible.

owner*: str** = ''*[](#pikepdf.models.Encryption.owner)
: 
The owner password to use. This allows full control
of the file. If blank, the PDF will be encrypted and
present as “(SECURED)” in PDF viewers. If the owner password
is blank, the user password should be as well.

user*: str** = ''*[](#pikepdf.models.Encryption.user)
: 
The user password to use. With this password, some
restrictions will be imposed by a typical PDF reader.
If blank, the PDF can be opened by anyone, but only modified
as allowed by the permissions in `allow`.

*class *pikepdf.models.Outline(*pdf*, *max_depth=15*, *strict=False*)[](#pikepdf.models.Outline)
: 
Maintains a intuitive interface for creating and editing PDF document outlines.

See {{ pdfrm }} section 12.3.

**Parameters:**

- 
**pdf** (*pikepdf._core.Pdf*) – PDF document object.

- 
**max_depth** (*int*) – Maximum recursion depth to consider when reading the outline.

- 
**strict** (*bool*) – If set to `False` (default) silently ignores structural errors.
Setting it to `True` raises a
`pikepdf.OutlineStructureError`
if any object references re-occur while the outline is being read or
written.

See also

[`pikepdf.Pdf.open_outline()`](main.html#pikepdf.Pdf.open_outline)

add(*title*, *destination*)[](#pikepdf.models.Outline.add)
: 
Add an item to the outline.

**Parameters:**

- 
**title** (*str*) – Title of the outline item.

- 
**destination** (*pikepdf.objects.Array** | **int** | **None*) – Destination to jump to when the item is selected.

**Returns:**
: 
The newly created [`OutlineItem`](#pikepdf.models.OutlineItem).

**Return type:**
: 
[OutlineItem](#pikepdf.models.OutlineItem)

*property *root*: list[[OutlineItem](#pikepdf.models.OutlineItem)]*[](#pikepdf.models.Outline.root)
: 
Return the root node of the outline.

**Return type:**

list[[OutlineItem](#pikepdf.models.OutlineItem)]

*class *pikepdf.models.OutlineItem(*title*, *destination=None*, *page_location=None*, *action=None*, *obj=None*, ***, *left=None*, *top=None*, *right=None*, *bottom=None*, *zoom=None*)[](#pikepdf.models.OutlineItem)
: 
Manage a single item in a PDF document outlines structure.

Includes nested items.

**Parameters:**

- 
**title** (*str*) – Title of the outlines item.

- 
**destination** (*pikepdf.objects.Array** | **pikepdf.objects.String** | **pikepdf.objects.Name** | **int** | **None*) – Page number, destination name, or any other PDF object
to be used as a reference when clicking on the outlines entry. Note
this should be `None` if an action is used instead. If set to a
page number, it will be resolved to a reference at the time of
writing the outlines back to the document.

- 
**page_location** (*PageLocation** | **str** | **None*) – Supplemental page location for a page number
in `destination`, e.g. `PageLocation.Fit`. May also be
a simple string such as `'FitH'`.

- 
**action** (*pikepdf.objects.Dictionary** | **None*) – Action to perform when clicking on this item. Will be ignored
during writing if `destination` is also set.

- 
**obj** (*pikepdf.objects.Dictionary** | **None*) – `Dictionary` object representing this outlines item in a `Pdf`.
May be `None` for creating a new object. If present, an existing
object is modified in-place during writing and original attributes
are retained.

- 
**left** (*float** | **None*) – Describes the viewport position associated
with a destination.

- 
**top** (*float** | **None*) – Describes the viewport position associated
with a destination.

- 
**bottom** (*float** | **None*) – Describes the viewport position associated
with a destination.

- 
**right** (*float** | **None*) – Describes the viewport position associated
with a destination.

- 
**zoom** (*float** | **None*) – Describes the viewport position associated
with a destination.

This object does not contain any information about higher-level or
neighboring elements.

**Valid destination arrays:**: 
[page /XYZ left top zoom]
generally
[page, PageLocationEntry, 0 to 4 ints]

action* = None*[](#pikepdf.models.OutlineItem.action)
: 

children*: list[[OutlineItem](#pikepdf.models.OutlineItem)]** = []*[](#pikepdf.models.OutlineItem.children)
: 

destination* = None*[](#pikepdf.models.OutlineItem.destination)
: 

*classmethod *from_dictionary_object(*obj*)[](#pikepdf.models.OutlineItem.from_dictionary_object)
: 
Create a `OutlineItem` from a `Dictionary`.

Does not process nested items.

**Parameters:**

**obj** (*pikepdf.objects.Dictionary*) – `Dictionary` object representing a single outline node.

is_closed* = False*[](#pikepdf.models.OutlineItem.is_closed)
: 

obj* = None*[](#pikepdf.models.OutlineItem.obj)
: 

page_location* = None*[](#pikepdf.models.OutlineItem.page_location)
: 

page_location_kwargs[](#pikepdf.models.OutlineItem.page_location_kwargs)
: 

title[](#pikepdf.models.OutlineItem.title)
: 

to_dictionary_object(*pdf*, *create_new=False*)[](#pikepdf.models.OutlineItem.to_dictionary_object)
: 
Create/update a `Dictionary` object from this outline node.

Page numbers are resolved to a page reference on the input
`Pdf` object.

**Parameters:**

- 
**pdf** (*pikepdf._core.Pdf*) – PDF document object.

- 
**create_new** (*bool*) – If set to `True`, creates a new object instead of
modifying an existing one in-place.

**Return type:**
: 
pikepdf.objects.Dictionary

*class *pikepdf.Permissions[](#pikepdf.Permissions)
: 
Stores the user-level permissions for an encrypted PDF.

A compliant PDF reader/writer should enforce these restrictions on people
who have the user password and not the owner password. In practice, either
password is sufficient to decrypt all document contents. A person who has
the owner password should be allowed to modify the document in any way.
pikepdf does not enforce the restrictions in any way; it is up to application
developers to enforce them as they see fit.

Unencrypted PDFs implicitly have all permissions allowed. Permissions can
only be changed when a PDF is saved.

accessibility*: bool** = True*[](#pikepdf.Permissions.accessibility)

Deprecated in PDF 2.0. Formerly used to block accessibility tools.

In older versions of the PDF specification, it was possible to request
a PDF reader to block a user’s right to use accessibility tools. Modern
PDF readers do not support this archaic feature and always allow accessibility
tools to be used. The only purpose of this permission is to provide
testing of this deprecated feature.

extract*: bool** = True*[](#pikepdf.Permissions.extract)
: 
Can users extract contents?

modify_annotation*: bool** = True*[](#pikepdf.Permissions.modify_annotation)
: 
Can users modify annotations?

modify_assembly*: bool** = False*[](#pikepdf.Permissions.modify_assembly)
: 
Can users arrange document contents?

modify_form*: bool** = True*[](#pikepdf.Permissions.modify_form)
: 
Can users fill out forms?

modify_other*: bool** = True*[](#pikepdf.Permissions.modify_other)
: 
Can users modify the document?

print_highres*: bool** = True*[](#pikepdf.Permissions.print_highres)
: 
Can users print the document at high resolution?

print_lowres*: bool** = True*[](#pikepdf.Permissions.print_lowres)
: 
Can users print the document at low resolution?

*class *pikepdf.models.EncryptionInfo(*encdict*)[](#pikepdf.models.EncryptionInfo)
: 
Reports encryption information for an encrypted PDF.

This information may not be changed, except when a PDF is saved.
This object is not used to specify the encryption settings to save
a PDF, due to non-overlapping information requirements.

**Parameters:**

**encdict** (*dict**[**str**, **Any**]*)

*property *P*: int*[](#pikepdf.models.EncryptionInfo.P)
: 
Return encoded permission bits.

See `Pdf.allow()` instead.

**Return type:**

int

*property *R*: int*[](#pikepdf.models.EncryptionInfo.R)
: 
Revision number of the security handler.

**Return type:**

int

*property *V*: int*[](#pikepdf.models.EncryptionInfo.V)
: 
Version of PDF password algorithm.

**Return type:**

int

*property *bits*: int*[](#pikepdf.models.EncryptionInfo.bits)
: 
Return the number of bits in the encryption algorithm.

e.g. if the algorithm is AES-256, this returns 256.

**Return type:**

int

*property *encryption_key*: bytes*[](#pikepdf.models.EncryptionInfo.encryption_key)
: 
Return the RC4 or AES encryption key used for this file.

**Return type:**

bytes

*property *file_method*: pikepdf._core.EncryptionMethod*[](#pikepdf.models.EncryptionInfo.file_method)
: 
Encryption method used to encode the whole file.

**Return type:**

pikepdf._core.EncryptionMethod

*property *stream_method*: pikepdf._core.EncryptionMethod*[](#pikepdf.models.EncryptionInfo.stream_method)
: 
Encryption method used to encode streams.

**Return type:**

pikepdf._core.EncryptionMethod

*property *string_method*: pikepdf._core.EncryptionMethod*[](#pikepdf.models.EncryptionInfo.string_method)
: 
Encryption method used to encode strings.

**Return type:**

pikepdf._core.EncryptionMethod

*property *user_password*: bytes*[](#pikepdf.models.EncryptionInfo.user_password)
: 
If possible, return the user password.

The user password can only be retrieved when a PDF is opened
with the owner password and when older versions of the
encryption algorithm are used.

The password is always returned as `bytes` even if it has
a clear Unicode representation.

**Return type:**

bytes

*class *pikepdf.AcroForm[](#pikepdf.AcroForm)
: 
A helper for working with PDF interactive forms.

add_and_rename_fields(*fields*)[](#pikepdf.AcroForm.add_and_rename_fields)

Add a collection of form fields.

Ensures that their fully qualified names don’t conflict with
already present form fields.

Fields within the collection of new fields that have the same name as
each other will continue to do so.

**Parameters:**

**fields** (*collections.abc.Sequence**[*[*AcroFormField*](#pikepdf.AcroFormField)*]*)

add_field(*field*)[](#pikepdf.AcroForm.add_field)
: 
Add a form field.

Initializes the document’s AcroForm dictionary if needed, and
updates the cache if necessary.

Note that you are adding fields that are copies of other fields, this
method may result in multiple fields existing with the same qualified
name, which can have unexpected side effects. In that case, you should
use `add_and_rename_fields()` instead.

**Parameters:**

**field** ([*AcroFormField*](#pikepdf.AcroFormField))

disable_digital_signatures()[](#pikepdf.AcroForm.disable_digital_signatures)
: 
Disables digital signature fields.

This method removes all digital signature fields from the document,
leaving any annotation showing the content of the field intact.

**Return type:**

None

*property *exists*: bool*[](#pikepdf.AcroForm.exists)
: 
True if the current document has an interactive form.

**Return type:**

bool

*property *fields*: collections.abc.Sequence[[AcroFormField](#pikepdf.AcroFormField)]*[](#pikepdf.AcroForm.fields)
: 
A list of all terminal fields in this interactive form.

Terminal fields are fields that have no children that are also fields.
Terminal fields should have children that are annotations, or be
annotations themselves. Only terminal fields are displayed as actual
widgets in the PDF document; non-terminal fields exist only for
grouping.

Intermediate nodes in the fields tree are not included in this list,
but you can still reach them through the pikepdf.AcroFormField.parent
and pikepdf.AcroFormField.top_level_field` properties.

**Return type:**

collections.abc.Sequence[[AcroFormField](#pikepdf.AcroFormField)]

fix_copied_annotations(*to_page*, *from_page*, *from_acroform*)[](#pikepdf.AcroForm.fix_copied_annotations)
: 
Copy form fields and annotations from one page to another.

This would typically be called after copying a new page in order to add
field/annotation awareness. When just copying the page by itself,
annotations end up being shared, and fields end up being omitted
because there is no reference to the field from the page. This method
ensures that each separate copy of a page has private annotations and
that fields and annotations are properly updated to resolve conflicts
that may occur from common resource and field names across documents.

**Parameters:**

- 
**to_page** ([*Page*](#pikepdf.Page)) – The page to copy to.

- 
**from_page** ([*Page*](#pikepdf.Page)) – The page to copy from. May be in a different PDF or in
the same PDF.

- 
**from_acroform** ([*AcroForm*](#pikepdf.AcroForm)) – The acroform object for the source PDF.

**Return type:**
: 
collections.abc.Sequence[[AcroFormField](#pikepdf.AcroFormField)]

Returns a list of newly created fields.

generate_appearances_if_needed()[](#pikepdf.AcroForm.generate_appearances_if_needed)
: 
Generate appearance streams for all form fields that need them.

For checkbox and radio button fields, this method ensures that
appearance state is consistent with the field’s value and uses any
pre-existing appearance streams.

If `needs_appearances` is False, this method does nothing.

This method uses the underlying QPDF implementation, which has several
limitations:

- 
Only supports ASCII characters in text fields

- 
Does not support multi-line text

- 
Ignores quadding (alignment)

**Return type:**

None

get_annotations_for_field(*field*)[](#pikepdf.AcroForm.get_annotations_for_field)
: 
Given a form field, return the associated annotation(s).

Typically, interactive forms store field information and annotation
information in the same dictionary, meaning this method will often
return a single pikepdf.Annotation which refers to the same
underlying pikepdf.Dictionary. However, this is not necessarily always
the case and should not be relied on. A field may store annotation data
in its own dictionary, and may even have multiple annotations.

**Parameters:**

**field** ([*AcroFormField*](#pikepdf.AcroFormField))

**Return type:**
: 
collections.abc.Sequence[[Annotation](#pikepdf.Annotation)]

get_field_for_annotation(*annotation*)[](#pikepdf.AcroForm.get_field_for_annotation)
: 
Given an annotation for a widget, return the associated form field.

Typically, interactive forms store field information and annotation
information in the same dictionary, meaning this method will often
return a pikepdf.AcroFormField which refers to the same underlying
pikepdf.Dictionary. However, this is not necessarily always
the case and should not be relied on. A field may store annotation data
in its own dictionary.

**Parameters:**

**annotation** ([*Annotation*](#pikepdf.Annotation))

**Return type:**
: 
[AcroFormField](#pikepdf.AcroFormField)

get_fields_with_qualified_name(*name*)[](#pikepdf.AcroForm.get_fields_with_qualified_name)
: 
Get a list of all fields with the given qualified name.

Generally, this list will contain only one member, as having multiple
fields with the same name is discouraged (but not impossible).

This will only return elements that have an explicit name (/T) in the
field dictionary. In practice, this means that it should return the
highest-level matching field, but not any children. (For example, this
method will return a radio group rather than individual radio buttons.)

**Parameters:**

**name** (*str*)

**Return type:**
: 
collections.abc.Sequence[[AcroFormField](#pikepdf.AcroFormField)]

get_form_fields_for_page(*page*)[](#pikepdf.AcroForm.get_form_fields_for_page)
: 
Find all the interactive form fields on a page.

In many PDFs, you may find that this returns a list that perfectly
corresponds to that returned by `get_widget_annotations_for_page`.
However, you should not rely on this behavior. This will not always be
the case. Use this method to get all the fields, then use the
`get_annotations_for_field` method for each to get the corresponding
annotations.

**Parameters:**

**page** ([*Page*](#pikepdf.Page))

**Return type:**
: 
collections.abc.Sequence[[AcroFormField](#pikepdf.AcroFormField)]

get_widget_annotations_for_page(*page*)[](#pikepdf.AcroForm.get_widget_annotations_for_page)
: 
Find all the interactive form widgets on a page.

In many PDFs, you may find that this returns a list that perfectly
corresponds to that returned by `get_form_fields_for_page`. However,
you should not rely on this behavior. This will not always be the case.
Use this method to get the annotations, then use the
`get_field_for_annotation` method for each to get the corresponding
field.

**Parameters:**

**page** ([*Page*](#pikepdf.Page))

**Return type:**
: 
collections.abc.Sequence[[Annotation](#pikepdf.Annotation)]

*property *needs_appearances*: bool*[](#pikepdf.AcroForm.needs_appearances)
: 
Indicates whether appearance streams must be regenerated.

This should be set to True if you modify any field values in the
interactive form, unless you also generate the appearance streams for
the modified fields.

**Return type:**

bool

remove_fields(*fields*)[](#pikepdf.AcroForm.remove_fields)
: 
Remove fields from the `fields` list.

**Parameters:**

**fields** (*collections.abc.Sequence**[*[*AcroFormField*](#pikepdf.AcroFormField)*]*)

set_field_name(*field*, *name*)[](#pikepdf.AcroForm.set_field_name)
: 
Set partial name of a field, updating internal records of field names.

**Parameters:**

- 
**field** ([*AcroFormField*](#pikepdf.AcroFormField))

- 
**name** (*str*)

*class *pikepdf.AcroFormField[](#pikepdf.AcroFormField)
: 
An AcroForm field. Wrapper around a PDF dictionary.

*property *alternate_name*: str*[](#pikepdf.AcroFormField.alternate_name)

The alternative field name (/TU), the field name presented to users.

If a value is not present in the underlying field, this property falls
back to the fully qualified name.

**Return type:**

str

*property *choices*: collections.abc.Sequence[str]*[](#pikepdf.AcroFormField.choices)
: 
Available choices for this field, if this is a choice field.

This does not contain choices for radio buttons. For radio buttons,
traverse the /Kids of the top-level field and inspect the individual
buttons.

This also only works for choice fields where the options are
represented as an array of strings. However, some PDFs represent
choices as an array of `[export_value, display_value]` pairs. This
is a limitation of the underlying QPDF library.
See [QPDF Issue 1433](https://github.com/qpdf/qpdf/issues/1433).
To get options for such fields, use field.obj.Opt instead.

**Return type:**

collections.abc.Sequence[str]

*property *default_appearance*: bytes*[](#pikepdf.AcroFormField.default_appearance)
: 
Default appearance string, inheriting from ancestor fields if needed.

This property will contain and empty string if the default appearance
string is not available (because it’s erroneously absent or because
this is not a variable text field). If not found in the field
hierarchy, look in /AcroForm.

**Return type:**

bytes

*property *default_resources*: pikepdf.objects.Dictionary*[](#pikepdf.AcroFormField.default_resources)
: 
The default resource dictionary for the field.

This comes not from the field but from the document-level /AcroForm
dictionary. While several PDF generates put a /DR key in the form
field’s dictionary, experimentation suggests that many popular
readers, including Adobe Acrobat and Acrobat Reader, ignore any /DR
item on the field.

**Return type:**

pikepdf.objects.Dictionary

*property *default_value[](#pikepdf.AcroFormField.default_value)
: 
The default value of the form field.

*property *default_value_as_string*: str*[](#pikepdf.AcroFormField.default_value_as_string)
: 
The field’s default value as a string.

If the value is not a string, this property will hold an empty string.

**Return type:**

str

*property *field_type*: str*[](#pikepdf.AcroFormField.field_type)
: 
The raw value of /FT if present, otherwise an empty string.

**Return type:**

str

*property *flags*: int*[](#pikepdf.AcroFormField.flags)
: 
Field flags from /Ff.

**Return type:**

int

*property *fully_qualified_name*: str*[](#pikepdf.AcroFormField.fully_qualified_name)
: 
The field’s fully qualified name.

This is defined as being the /T (partial_name) value of this and all
ancestors, concatenated together with dots.

**Return type:**

str

generate_appearance(*annot*)[](#pikepdf.AcroFormField.generate_appearance)
: 
Generate an appearance stream for this field.

**Parameters:**

**annot** ([*Annotation*](#pikepdf.Annotation))

get_inheritable_field_value(*name*)[](#pikepdf.AcroFormField.get_inheritable_field_value)
: 
Get field value, possibly inheriting the value from ancestor node.

**Parameters:**

**name** (*str*)

get_inheritable_field_value_as_name(*name*)[](#pikepdf.AcroFormField.get_inheritable_field_value_as_name)
: 
Get an inherited field value as a Name object.

If the value is not a name, this property will hold an empty name.

**Parameters:**

**name** (*str*)

**Return type:**
: 
pikepdf.objects.Name

get_inheritable_field_value_as_string(*name*)[](#pikepdf.AcroFormField.get_inheritable_field_value_as_string)
: 
Get an inherited field value as a string.

If the value is not a string, this property will hold an empty string.

**Parameters:**

**name** (*str*)

**Return type:**
: 
str

*property *is_checkbox*: bool*[](#pikepdf.AcroFormField.is_checkbox)
: 
True if field is type /Btn and flags do not indicate other type of button.

**Return type:**

bool

*property *is_checked*: bool*[](#pikepdf.AcroFormField.is_checked)
: 
True if field is a checkbox and is checked.

**Return type:**

bool

*property *is_choice*: bool*[](#pikepdf.AcroFormField.is_choice)
: 
True if fields if of type /Ch.

**Return type:**

bool

*property *is_null*: bool*[](#pikepdf.AcroFormField.is_null)
: 
True if the field is null.

**Return type:**

bool

*property *is_pushbutton*: bool*[](#pikepdf.AcroFormField.is_pushbutton)
: 
True if field is of type /Btn and flags indicate that a pushbutton.

**Return type:**

bool

*property *is_radio_button*: bool*[](#pikepdf.AcroFormField.is_radio_button)
: 
True if field is of type /Btn and flags indicate that a radio button.

**Return type:**

bool

*property *is_text*: bool*[](#pikepdf.AcroFormField.is_text)
: 
True if field is of type /Tx.

**Return type:**

bool

*property *mapping_name*: str*[](#pikepdf.AcroFormField.mapping_name)
: 
Return the mapping field name (/TM).

If a value is not present in the underlying field, this property falls
back to the fully qualified name.

**Return type:**

str

*property *parent*: [AcroFormField](#pikepdf.AcroFormField)*[](#pikepdf.AcroFormField.parent)
: 
This field’s parent.

If there is no parent, a AcroFormField where `field.is_null is True` is
returned.

**Return type:**

[AcroFormField](#pikepdf.AcroFormField)

*property *partial_name*: str*[](#pikepdf.AcroFormField.partial_name)
: 
The field’s partial name (/T).

**Return type:**

str

*property *quadding*: int*[](#pikepdf.AcroFormField.quadding)
: 
The quadding value, inheriting from ancestor fields if needed.

This will be 0 if the quadding is not specified. Look in /AcroForm if
not found in the field hierarchy.

**Return type:**

int

set_value(*value*, *need_appearance=True*)[](#pikepdf.AcroFormField.set_value)
: 
Set the `value` property.

If `need_appearance` is true, and this is a text or choice field, the
`pikepdf.AcroForm.needs_appearances` will also be set.

**Parameters:**

**need_appearance** (*bool*)

*property *top_level_field*: [AcroFormField](#pikepdf.AcroFormField)*[](#pikepdf.AcroFormField.top_level_field)
: 
The top-level field for this field.

This will be the field itself, or one of its ancestors (often the
immediate parent).

Note that the top-level field may not itself be a “real” field. Fields
may be nested underneath one another at any arbitrary level, with the
outer fields forming groups or sets of fields. This property references
the highest field in this field’s hierarchy.

**Return type:**

[AcroFormField](#pikepdf.AcroFormField)

*property *value[](#pikepdf.AcroFormField.value)
: 
The current value of the form field.

*property *value_as_string*: str*[](#pikepdf.AcroFormField.value_as_string)
: 
The field’s value as a string.

If the value is not a string, this property will hold an empty string.

**Return type:**

str

*class *pikepdf.Annotation(*obj*)[](#pikepdf.Annotation)
: 
A PDF annotation. Wrapper around a PDF dictionary.

Describes an annotation in a PDF, such as a comment, underline,
copy editing marks, interactive widgets, redactions, 3D objects, sound
and video clips.

See the {{ pdfrm }} section 12.5.6 for the full list of annotation types
and definition of terminology.

Added in version 2.12.

**Parameters:**

**obj** ([*Object*](main.html#pikepdf.Object))

*property *appearance_dict*: [Object](main.html#pikepdf.Object)*[](#pikepdf.Annotation.appearance_dict)
: 
Returns the annotations appearance dictionary.

**Return type:**

[Object](main.html#pikepdf.Object)

*property *appearance_state*: [Object](main.html#pikepdf.Object)*[](#pikepdf.Annotation.appearance_state)
: 
Returns the annotation’s appearance state (or None).

For a checkbox or radio button, the appearance state may be `pikepdf.Name.On`
or `pikepdf.Name.Off`.

**Return type:**

[Object](main.html#pikepdf.Object)

*property *flags*: int*[](#pikepdf.Annotation.flags)
: 
Returns the annotation’s flags.

**Return type:**

int

get_appearance_stream(*which*, *state=...*)[](#pikepdf.Annotation.get_appearance_stream)
: 
Returns one of the appearance streams associated with an annotation.

**Parameters:**

- 
**which** ([*Object*](main.html#pikepdf.Object)) – Usually one of `pikepdf.Name.N`, `pikepdf.Name.R` or
`pikepdf.Name.D`, indicating the normal, rollover or down
appearance stream, respectively. If any other name is passed,
an appearance stream with that name is returned.

- 
**state** ([*Object*](main.html#pikepdf.Object)* | **None*) – The appearance state. For checkboxes or radio buttons, the
appearance state is usually whether the button is on or off.

**Return type:**
: 
[Object](main.html#pikepdf.Object)

get_page_content_for_appearance(*name*, *rotate*, *required_flags=...*, *forbidden_flags=...*)[](#pikepdf.Annotation.get_page_content_for_appearance)
: 
Generate content stream text that draws this annotation as a Form XObject.

**Parameters:**

- 
**name** (*pikepdf.objects.Name*) – What to call the object we create.

- 
**rotate** (*int*) – Should be set to the page’s /Rotate value or 0.

- 
**required_flags** (*int*) – The required appearance flags. See PDF reference manual.

- 
**forbidden_flags** (*int*) – The forbidden appearance flags. See PDF reference manual.

**Return type:**
: 
bytes

Note

This method is done mainly with qpdf. Its behavior may change when
different qpdf versions are used.

*property *obj*: [Object](main.html#pikepdf.Object)*[](#pikepdf.Annotation.obj)
: 

**Return type:**

[Object](main.html#pikepdf.Object)

*property *rect*: [Rectangle](main.html#pikepdf.Rectangle)*[](#pikepdf.Annotation.rect)
: 
Returns a rectangle defining the location of the annotation.

**Return type:**

[Rectangle](main.html#pikepdf.Rectangle)

*property *subtype*: str*[](#pikepdf.Annotation.subtype)
: 
Returns the subtype of this annotation.

**Return type:**

str

*class *pikepdf._core.Attachments(**args*, ***kwargs*)[](#pikepdf._core.Attachments)
: 
Exposes files attached to a PDF.

If a file is attached to a PDF, it is exposed through this interface.
For example `p.attachments['readme.txt']` would return a
`pikepdf._core.AttachedFileSpec` that describes the attached file,
if a file were attached under that name.
`p.attachments['readme.txt'].get_file()` would return a
[`pikepdf._core.AttachedFile`](#pikepdf._core.AttachedFile), an archaic intermediate object to support
different versions of the file for different platforms. Typically one
just calls `p.attachments['readme.txt'].read_bytes()` to get the
contents of the file.

This interface provides access to any files that are attached to this PDF,
exposed as a Python `collections.abc.MutableMapping` interface.

The keys (virtual filenames) are always `str`, and values are always
[`pikepdf.AttachedFileSpec`](#pikepdf.AttachedFileSpec).

To create a new attached file, use
`pikepdf._core.AttachedFileSpec.from_filepath()`
to create a `pikepdf._core.AttachedFileSpec` and then assign it to the
[`pikepdf.Pdf.attachments`](main.html#pikepdf.Pdf.attachments) mapping. If the file is in memory, use
`p.attachments['test.pdf'] = b'binary data'`.

Use this interface through [`pikepdf.Pdf.attachments`](main.html#pikepdf.Pdf.attachments).

Added in version 3.0.

Changed in version 8.10.1: Added convenience interface for directly loading attached files, e.g.
`pdf.attachments['/test.pdf'] = b'binary data'`. Prior to this release,
there was no way to attach data in memory as a file.

*class *pikepdf.AttachedFileSpec(*pdf*, *data*, ***, *description*, *filename*, *mime_type*, *creation_date*, *mod_date*)[](#pikepdf.AttachedFileSpec)
: 
In a PDF, a file specification provides name and metadata for a target file.

Most file specifications are *simple* file specifications, and contain only
one attached file. Call [`get_file()`](#pikepdf.AttachedFileSpec.get_file) to get the attached file:

```
pdf = Pdf.open(...)

fs = pdf.attachments[&#39;example.txt&#39;]
stream = fs.get_file()

```

To attach a new file to a PDF, you may construct a `AttachedFileSpec`.

```
pdf = Pdf.open(...)

fs = AttachedFileSpec.from_filepath(pdf, Path(&#39;somewhere/spreadsheet.xlsx&#39;))

pdf.attachments[&#39;spreadsheet.xlsx&#39;] = fs

```

PDF supports the concept of having multiple, platform-specialized versions of the
attached file (similar to resource forks on some operating systems). In theory,
this attachment ought to be the same file, but
encoded in different ways. For example, perhaps a PDF includes a text file encoded
with Windows line endings (`\r\n`) and a different one with POSIX line endings
(`\n`). Similarly, PDF allows for the possibility that you need to encode
platform-specific filenames. pikepdf cannot directly create these, because they
are arguably obsolete; it can provide access to them, however.

If you have to deal with platform-specialized versions,
use [`get_all_filenames()`](#pikepdf.AttachedFileSpec.get_all_filenames) to enumerate those available.

Described in the {{ pdfrm }} section 7.11.3.

Added in version 3.0.

**Parameters:**

- 
**pdf** ([*Pdf*](main.html#pikepdf.Pdf))

- 
**data** (*bytes*)

- 
**description** (*str*)

- 
**filename** (*str*)

- 
**mime_type** (*str*)

- 
**creation_date** (*str*)

- 
**mod_date** (*str*)

__init__(*pdf*, *data*, ***, *description*, *filename*, *mime_type*, *creation_date*, *mod_date*)[](#pikepdf.AttachedFileSpec.__init__)
: 
Construct a attached file spec from data in memory.

To construct a file spec from a file on the computer’s file system,
use [`from_filepath()`](#pikepdf.AttachedFileSpec.from_filepath).

**Parameters:**

- 
**pdf** ([*Pdf*](main.html#pikepdf.Pdf)) – The Pdf to attach this file specification to.

- 
**data** (*bytes*) – Resource to load.

- 
**description** (*str*) – Any description text for the attachment. May be
shown in PDF viewers.

- 
**filename** (*str*) – Filename to display in PDF viewers.

- 
**mime_type** (*str*) – Helps PDF viewers decide how to display the information.

- 
**creation_date** (*str*) – PDF date string for when this file was created.

- 
**mod_date** (*str*) – PDF date string for when this file was last modified.

- 
**relationship** – A [`pikepdf.Name`](main.html#pikepdf.Name) indicating the relationship
of this file to the document. Canonically, this should be a name
from the PDF specification:
Source, Data, Alternative, Supplement, EncryptedPayload, FormData,
Schema, Unspecified. If omitted, Unspecified is used.

**Return type:**
: 
None

*property *description*: str*[](#pikepdf.AttachedFileSpec.description)
: 
Description text associated with the embedded file.

**Return type:**

str

*property *filename*: str*[](#pikepdf.AttachedFileSpec.filename)
: 
The main filename for this file spec.

In priority order, getting this returns the first of /UF, /F, /Unix,
/DOS, /Mac if multiple filenames are set. Setting this will set a UTF-8
encoded Unicode filename and write it to /UF.

**Return type:**

str

*static *from_filepath(*pdf*, *path*, ***, *description=''*)[](#pikepdf.AttachedFileSpec.from_filepath)
: 
Construct a file specification from a file path.

This function will automatically add a creation and modified date
using the file system, and a MIME type inferred from the file’s extension.

If the data required for the attach is in memory, use
[`pikepdf.AttachedFileSpec()`](#pikepdf.AttachedFileSpec) instead.

**Parameters:**

- 
**pdf** ([*Pdf*](main.html#pikepdf.Pdf)) – The Pdf to attach this file specification to.

- 
**path** (*pathlib.Path** | **str*) – A file path for the file to attach to this Pdf.

- 
**description** (*str*) – An optional description. May be shown to the user in
PDF viewers.

- 
**relationship** – An optional relationship type. May be used to
indicate the type of attachment, e.g. Name.Source or Name.Data.
Canonically, this should be a name from the PDF specification:
Source, Data, Alternative, Supplement, EncryptedPayload, FormData,
Schema, Unspecified. If omitted, Unspecified is used.

**Return type:**
: 
[AttachedFileSpec](#pikepdf.AttachedFileSpec)

get_all_filenames()[](#pikepdf.AttachedFileSpec.get_all_filenames)
: 
Return a Python dictionary that describes all filenames.

The returned dictionary is not a pikepdf Object.

Multiple filenames are generally a holdover from the pre-Unicode era.
Modern PDFs can generally set UTF-8 filenames and avoid using
punctuation or other marks that are forbidden in filenames.

**Return type:**

dict

get_file(*name=...*)[](#pikepdf.AttachedFileSpec.get_file)
: 
Return an attached file.

Typically, only one file is attached to an attached file spec.
When multiple files are attached, use the `name` parameter to
specify which one to return.

**Parameters:**

**name** (*pikepdf.objects.Name*) – Typical names would be `/UF` and `/F`. See {{ pdfrm }}
for other obsolete names.

**Return type:**
: 
[AttachedFile](#pikepdf._core.AttachedFile)

*property *obj*: pikepdf.objects.Dictionary*[](#pikepdf.AttachedFileSpec.obj)
: 
Get the underlying PDF object (typically a Dictionary).

**Return type:**

pikepdf.objects.Dictionary

*property *relationship*: pikepdf.objects.Name | None*[](#pikepdf.AttachedFileSpec.relationship)
: 
Describes the relationship of this attached file to the PDF.

**Return type:**

pikepdf.objects.Name | None

*class *pikepdf._core.AttachedFile[](#pikepdf._core.AttachedFile)
: 
An object that contains an actual attached file.

These objects do not need to be created manually; they are normally part of an
AttachedFileSpec.

Added in version 3.0.

creation_date*: datetime.datetime | None*[](#pikepdf._core.AttachedFile.creation_date)

*property *md5*: bytes*[](#pikepdf._core.AttachedFile.md5)
: 
Get the MD5 checksum of attached file according to the PDF creator.

**Return type:**

bytes

mime_type*: str*[](#pikepdf._core.AttachedFile.mime_type)
: 
Get the MIME type of the attached file according to the PDF creator.

mod_date*: datetime.datetime | None*[](#pikepdf._core.AttachedFile.mod_date)
: 

*property *obj*: [Object](main.html#pikepdf.Object)*[](#pikepdf._core.AttachedFile.obj)
: 

**Return type:**

[Object](main.html#pikepdf.Object)

read_bytes()[](#pikepdf._core.AttachedFile.read_bytes)
: 

**Return type:**

bytes

*property *size*: int*[](#pikepdf._core.AttachedFile.size)
: 
Get length of the attached file in bytes according to the PDF creator.

**Return type:**

int

*class *pikepdf.NameTree(*obj*, ***, *auto_repair=...*)[](#pikepdf.NameTree)
: 
An object for managing *name tree* data structures in PDFs.

A name tree is a key-value data structure. The keys are any binary strings
(that is, Python `bytes`). If `str` selected is provided as a key,
the UTF-8 encoding of that string is tested. Name trees are (confusingly)
not indexed by `pikepdf.Name` objects. They behave like
`DictMapping[bytes, pikepdf.Object]`.

The keys are sorted; pikepdf will ensure that the order is preserved.

The value may be any PDF object. Typically it will be a dictionary or array.

Internally in the PDF, a name tree can be a fairly complex tree data structure
implemented with many dictionaries and arrays. pikepdf (using libqpdf)
will automatically read, repair and maintain this tree for you. There should not
be any reason to access the internal nodes of a number tree; use this
interface instead.

NameTrees are used to store certain objects like file attachments in a PDF.
Where a more specific interface exists, use that instead, and it will
manipulate the name tree in a semantic correct manner for you.

Do not modify the internal structure of a name tree while you have a
`NameTree` referencing it. Access it only through the `NameTree` object.

Names trees are described in the {{ pdfrm }} section 7.9.6. See section 7.7.4
for a list of PDF objects that are stored in name trees.

Added in version 3.0.

**Parameters:**

- 
**obj** ([*Object*](main.html#pikepdf.Object))

- 
**auto_repair** (*bool*)

*static *new(*pdf*, ***, *auto_repair=True*)[](#pikepdf.NameTree.new)
: 
Create a new NameTree in the provided Pdf.

You will probably need to insert the name tree in the PDF’s
catalog. For example, to insert this name tree in
/Root /Names /Dests:

```
nt = NameTree.new(pdf)
pdf.Root.Names.Dests = nt.obj

```

**Parameters:**

- 
**pdf** ([*Pdf*](main.html#pikepdf.Pdf))

- 
**auto_repair** (*bool*)

**Return type:**
: 
[NameTree](#pikepdf.NameTree)

*property *obj*: [Object](main.html#pikepdf.Object)*[](#pikepdf.NameTree.obj)
: 
Returns the underlying root object for this name tree.

**Return type:**

[Object](main.html#pikepdf.Object)

*class *pikepdf.NumberTree(*obj*, ***, *auto_repair=...*)[](#pikepdf.NumberTree)
: 
An object for managing *number tree* data structures in PDFs.

A number tree is a key-value data structure, like name trees, except that the
key is an integer. It behaves like `Dict[int, pikepdf.Object]`.

The keys can be sparse - not all integers positions will be populated. Keys
are also always sorted; pikepdf will ensure that the order is preserved.

The value may be any PDF object. Typically it will be a dictionary or array.

Internally in the PDF, a number tree can be a fairly complex tree data structure
implemented with many dictionaries and arrays. pikepdf (using libqpdf)
will automatically read, repair and maintain this tree for you. There should not
be any reason to access the internal nodes of a number tree; use this
interface instead.

NumberTrees are not used much in PDF. The main thing they provide is a mapping
between 0-based page numbers and user-facing page numbers (which pikepdf
also exposes as `Page.label`). The `/PageLabels` number tree is where the
page numbering rules are defined.

Number trees are described in the {{ pdfrm }} section 7.9.7. See section 12.4.2
for a description of the page labels number tree. Here is an example of modifying
an existing page labels number tree:

```
pagelabels = NumberTree(pdf.Root.PageLabels)
# Label pages starting at 0 with lowercase Roman numerals
pagelabels[0] = Dictionary(S=Name.r)
# Label pages starting at 6 with decimal numbers
pagelabels[6] = Dictionary(S=Name.D)

# Page labels will now be:
# i, ii, iii, iv, v, 1, 2, 3, ...

```

Do not modify the internal structure of a name tree while you have a
`NumberTree` referencing it. Access it only through the `NumberTree` object.

Added in version 5.4.

**Parameters:**

- 
**obj** ([*Object*](main.html#pikepdf.Object))

- 
**auto_repair** (*bool*)

*static *new(*pdf*, ***, *auto_repair=True*)[](#pikepdf.NumberTree.new)
: 
Create a new NumberTree in the provided Pdf.

You will probably need to insert the number tree in the PDF’s
catalog. For example, to insert this number tree in
/Root /PageLabels:

```
nt = NumberTree.new(pdf)
pdf.Root.PageLabels = nt.obj

```

**Parameters:**

- 
**pdf** ([*Pdf*](main.html#pikepdf.Pdf))

- 
**auto_repair** (*bool*)

**Return type:**
: 
[NumberTree](#pikepdf.NumberTree)

*property *obj*: [Object](main.html#pikepdf.Object)*[](#pikepdf.NumberTree.obj)
: 

**Return type:**

[Object](main.html#pikepdf.Object)

---
# Page
Source: https://pikepdf.readthedocs.io/en/latest/topics/page.html

# Working with pages[](#working-with-pages)

This section details with how to view and edit the contents of a page.

pikepdf is not an ideal tool for producing new PDFs from scratch – and there are
many good tools for that, as mentioned elsewhere. pikepdf is better at inspecting,
editing and transforming existing PDFs.

`pikepdf.Page` objects can be thought of a subclass of `pikepdf.Dictionary`. Since
pages are important, they are special objects, and the `Pdf.pages` API will only
accept or return pikepdf.Page.

```
&gt;&gt;&gt; from pikepdf import Pdf, Page

&gt;&gt;&gt; example = Pdf.open(&#39;../tests/resources/congress.pdf&#39;)

&gt;&gt;&gt; page1 = example.pages[0]

&gt;&gt;&gt; page1
&lt;pikepdf.Page({
  &quot;/Contents&quot;: pikepdf.Stream(owner=&lt;...&gt;, data=b&#39;q\n200.0000 0 0 304.0&#39;..., {
    &quot;/Length&quot;: 50
  }),
  &quot;/MediaBox&quot;: [ 0, 0, 200, 304 ],
  &quot;/Parent&quot;: &lt;reference to /Pages&gt;,
  &quot;/Resources&quot;: {
    &quot;/XObject&quot;: {
      &quot;/Im0&quot;: pikepdf.Stream(owner=&lt;...&gt;, data=&lt;...&gt;, {
        &quot;/BitsPerComponent&quot;: 8,
        &quot;/ColorSpace&quot;: &quot;/DeviceRGB&quot;,
        &quot;/Filter&quot;: [ &quot;/DCTDecode&quot; ],
        &quot;/Height&quot;: 1520,
        &quot;/Length&quot;: 192956,
        &quot;/Subtype&quot;: &quot;/Image&quot;,
        &quot;/Type&quot;: &quot;/XObject&quot;,
        &quot;/Width&quot;: 1000
      })
    }
  },
  &quot;/Type&quot;: &quot;/Page&quot;
})&gt;

```

The page’s `/Contents` key contains instructions for drawing the page content.
This is a [content stream](streams.html), which is a stream object
that follows special rules.

Also attached to this page is a `/Resources` dictionary, which contains a
single XObject image. The image is compressed with the `/DCTDecode` filter,
meaning it is encoded with the DCT, so it is
a JPEG. pikepdf has special APIs for [working with images](images.html).

The `/MediaBox` describes the bounding box of the page in PDF pt units
(1/72” or 0.35 mm).

You *can* access the page dictionary data structure directly, but it’s fairly
complicated. There are a number of rules, optional values and implied values.
To do so, you would access the `page1.obj` property, which returns the
underlying dictionary object that holds the page data.

Changed in version 9.0: The `Pdf.pages` API was made strict, and now accepts only pikepdf.Page
for its various functions. In most cases, if you intend to create a
Dictionary and use it as a page, all you need to do is be explicit:
``pikepdf.Page(pikepdf.Dictionary(Type=Name.Page))`

Changed in version 8.x: The use of Python dictionary or pikepdf.Dictionary to represent pages
was deprecated.

Changed in version 2.x: In pikepdf 2.x, the raw dictionary object was returned, and it was
necessary to manually wrap it with the support model:
`page = Page(pdf.pages[0])`. This is no longer necessary.

## Page boxes[](#page-boxes)

```
&gt;&gt;&gt; page1.trimbox
pikepdf.Array([ 0, 0, 200, 304 ])

```

`Page` will resolve implicit information. For example, `page.trimbox`
will return an appropriate trim box for this page, which in this case is
equal to the media box. This happens even if the page does not define
a trim box.

---
# Content Streams
Source: https://pikepdf.readthedocs.io/en/latest/topics/content_streams.html

# Working with content streams[](#working-with-content-streams)

A content stream is a stream object associated with either a page or a Form
XObject that describes where and how to draw images, vectors, and text. (These
PDF streams have nothing to do with Python I/O streams.)

Content streams are binary data that can be thought of as a list of operators
and zero or more operands. Operands are given first, followed by the operator.
It is a stack-based language, loosely based on PostScript. (It’s not actually
PostScript, but sometimes well-meaning people mistakenly say that it is!)
Like HTML, it has a precise grammar, and also like (pure) HTML, it has no loops,
conditionals or variables.

A typical example is as follows (with additional whitespace and PostScript-style
`%`-comments):

```
q                   % 1. Push graphics stack.
100 0 0 100 0 0 cm  % 2. The 6 numbers are the operands, followed by cm operator.
                    %    This configures the current transformation matrix.
/Image1 Do          % 3. Draw the object named /Image1 from the /Resources
                    %    dictionary.
Q                   % 4. Pop graphics stack.

```

The pattern `q, cm, &lt;drawing commands&gt;, Q` is extremely common. The drawing
commands may recurse with another `q, cm, ..., Q`.

pikepdf provides a C++ optimized content stream parser and a filter. The parser
is best used for reading and interpreting content streams; the filter is better
for low level editing.

## Pretty-printing content streams[](#pretty-printing-content-streams)

To pretty-print a content stream, you can use parse and then unparse it. This
converts it from binary data form to pikepdf objects and back. In the process,
the content stream is cleaned up. Every instruction will be separated by a line
break.

```
with pikepdf.open(&quot;../tests/resources/congress.pdf&quot;) as pdf:
    page = pdf.pages[0]
    instructions = pikepdf.parse_content_stream(page)
    data = pikepdf.unparse_content_stream(instructions)
    print(data.decode(&#39;ascii&#39;))

```

Note

Content streams are not always decodable to ASCII. This one just happens to be.

---
# Images
Source: https://pikepdf.readthedocs.io/en/latest/topics/images.html

# Working with images[](#working-with-images)

PDFs embed images as binary stream objects within the PDF’s data stream. The
stream object’s dictionary describes properties of the image such as its
dimensions and color space. The same image may be drawn multiple times on
multiple pages, at different scales and positions.

In some cases such as JPEG2000, the standard file format of the image
is used verbatim, even when the file format contains headers and information
that is repeated in the stream dictionary. In other cases such as for
PNG-style encoding, the image file format is not used directly.

pikepdf currently has no facility to embed new images into PDFs. We recommend
img2pdf instead, because it does the job so well. pikepdf instead allows
for image inspection and lossless/transcode free (where possible) “pdf2img”.

pikepdf also cannot extract vector images, that is images produced through a
combination of PDF drawing commands. These are produced by a content stream,
or sometimes a Form XObject. Unfortunately there may not be anything in the
PDF that indicates a particular sequence of operations produces an image,
and that sequence is not necessarily all in the same place. To extract a
vector image, use a PDF viewer/editor to crop to that image.

## Playing with images[](#playing-with-images)

pikepdf provides a helper class [`PdfImage`](../api/models.html#pikepdf.PdfImage) for manipulating
images in a PDF. The helper class helps manage the complexity of the image
dictionaries.

```
&gt;&gt;&gt; from pikepdf import Pdf, PdfImage, Name

&gt;&gt;&gt; example = Pdf.open(&#39;../tests/resources/congress.pdf&#39;)

&gt;&gt;&gt; page1 = example.pages[0]

&gt;&gt;&gt; list(page1.images.keys())
[&#39;/Im0&#39;]

&gt;&gt;&gt; rawimage = page1.images[&#39;/Im0&#39;]  # The raw object/dictionary

&gt;&gt;&gt; pdfimage = PdfImage(rawimage)

&gt;&gt;&gt; type(pdfimage)
&lt;class &#39;pikepdf.models.image.PdfImage&#39;&gt;

```

In Jupyter (or IPython with a suitable backend) the image will be
displayed.

You can also inspect the properties of the image. The parameters are similar
to Pillow’s.

```
&gt;&gt;&gt; pdfimage.colorspace
&#39;/DeviceRGB&#39;

&gt;&gt;&gt; pdfimage.width, pdfimage.height
(1000, 1520)

```

Note

`.width` and `.height` are the resolution of the image in pixels, not
the size of the image in page coordinates. The size of the image in page
coordinates is determined by the content stream.

---
# Settings
Source: https://pikepdf.readthedocs.io/en/latest/api/settings.html

# Settings[](#settings)

Some of pikepdf’s global parameters can be tuned.

pikepdf.settings.get_decimal_precision()[](#pikepdf.settings.get_decimal_precision)
: 
Set the number of decimal digits to use when converting floats.

**Return type:**

int

pikepdf.settings.set_decimal_precision(*prec*)[](#pikepdf.settings.set_decimal_precision)
: 
Get the number of decimal digits to use when converting floats.

**Parameters:**

**prec** (*int*)

**Return type:**
: 
int

pikepdf.settings.set_flate_compression_level(*level*)[](#pikepdf.settings.set_flate_compression_level)
: 
Set compression level whenever Flate compression is used.

**Parameters:**

**level** (*Literal**[**-1**, **0**, **1**, **2**, **3**, **4**, **5**, **6**, **7**, **8**, **9**]*) – -1 (default), 0 (no compression), 1 to 9 (increasing compression)

**Return type:**
: 
int

---
# Arch
Source: https://pikepdf.readthedocs.io/en/latest/references/arch.html

# Architecture[](#architecture)

pikepdf uses [pybind11](https://github.com/pybind/pybind11) to bind the
C++ interface of QPDF. pybind11 was selected after evaluating Cython, CFFI and
SWIG as possible binding solutions.

In addition to bindings pikepdf includes support code written in a mix of C++
and Python, mainly to present a clean Pythonic interface to C++ and implement
higher level functionality.

## Internals[](#internals)

Internally the package presents a module named `pikepdf` from which objects
can be imported. The C++ extension module is currently named `pikepdf._core`.
Users of `pikepdf` should not directly access `_core` since it is an
internal interface. In previous versions, this library was named `_qpdf`.

In general, modules or objects behind an underscore are private (although they
may be returned in some situations).

## Thread safety[](#thread-safety)

Because of the global interpreter lock (GIL), it is safe to read pikepdf
objects across Python threads. Also because of the GIL, there may not be much
performance gain from doing so.

If one or more threads will be modifying pikepdf objects, you will have to
coordinate read and write access with a `threading.Lock`.

It is not currently possible to pickle pikepdf objects or marshall them across
process boundaries (as would be required to use pikepdf in
`multiprocessing`). If this were implemented, it would not be much more
efficient than saving a full PDF and sending it to another process.
Parallelizing work (for example, by dividing work by PDF pages) can still be
achieved by having each worker process open the same file.

## File handles[](#file-handles)

Because of technical limitations in underlying libraries, pikepdf keeps the
source PDF file open when a content is copied from it to another PDF, even when
all Python variables pointing to the source are removed. If a PDF is being
assembled from many sources, then all of those sources are held open in memory.

---
# Resources
Source: https://pikepdf.readthedocs.io/en/latest/references/resources.html

# Resources[](#resources)

- 
[qpdf manual](https://qpdf.readthedocs.io/)

- 
[PDF 1.7](https://opensource.adobe.com/dc-acrobat-sdk-docs/standards/pdfstandards/pdf/PDF32000_2008.pdf) ISO Specification PDF 32000-1:2008

- 
[Adobe Supplement to ISO 32000 BaseVersion 1.7 ExtensionLevel 3](https://www.adobe.com/content/dam/acom/en/devnet/pdf/adobe_supplement_iso32000.pdf), Adobe Acrobat 9.0, June 2008, for AESv3

- 
Other [Adobe extensions](https://www.adobe.com/devnet/pdf/pdf_reference.html) to the PDF specification

For information about copyrights and licenses, including those associated with the
images in this documentation, see the source tree file `.reuse/dep5`.

---
# Filters
Source: https://pikepdf.readthedocs.io/en/latest/api/filters.html

# Content streams[](#content-streams)

In PDF, drawing operations are all performed in content streams that describe
the positioning and drawing order of all graphics (including text, images and
vector drawing).

See also

[Working with content streams](../topics/content_streams.html#working-with-content-streams)

pikepdf (and libqpdf) provide two tools for interpreting content streams:
a parser and filter. The parser returns higher level information, conveniently
grouping all commands with their operands. The parser is useful when one wants
to retrieve information from a content stream, such as determine the position
of an element. The parser should not be used to edit or reconstruct the content
stream because some subtleties are lost in parsing.

The token filter works at a lower level, considering each token including
comments, and distinguishing different types of spaces. This allows modifying
content streams. A TokenFilter must be subclassed; the specialized version
describes how it should transform the stream of tokens.

## Content stream parsers[](#content-stream-parsers)

pikepdf.parse_content_stream(*page_or_stream*, *operators=''*)[](#pikepdf.parse_content_stream)
: 
Parse a PDF content stream into a sequence of instructions.

A PDF content stream is list of instructions that describe where to render
the text and graphics in a PDF. This is the starting point for analyzing
PDFs.

If the input is a page and page.Contents is an array, then the content
stream is automatically treated as one coalesced stream.

Each instruction contains at least one operator and zero or more operands.

This function does not have anything to do with opening a PDF file itself or
processing data from a whole PDF. It is for processing a specific object inside
a PDF that is already opened.

**Parameters:**

- 
**page_or_stream** (*pikepdf._core.Object** | **pikepdf._core.Page*) – A page object, or the content
stream attached to another object such as a Form XObject.

- 
**operators** (*str*) – A space-separated string of operators to whitelist.
For example ‘q Q cm Do’ will return only operators
that pertain to drawing images. Use ‘BI ID EI’ for inline images.
All other operators and associated tokens are ignored. If blank,
all tokens are accepted.

**Return type:**
: 
list[ContentStreamInstructions]

Example

```
&gt;&gt;&gt; with pikepdf.Pdf.open(&quot;../tests/resources/pal-1bit-trivial.pdf&quot;) as pdf:
...     page = pdf.pages[0]
...     for operands, command in pikepdf.parse_content_stream(page):
...         print(command)
q
cm
Do
Q

```

Changed in version 3.0: Returns a list of `ContentStreamInstructions` instead of a list
of (operand, operator) tuples. The returned items are duck-type compatible
with the previous returned items.

pikepdf.unparse_content_stream(*instructions*)[](#pikepdf.unparse_content_stream)
: 
Convert collection of instructions to bytes suitable for storing in PDF.

Given a parsed list of instructions/operand-operators, convert to bytes suitable
for embedding in a PDF. In PDF the operator always follows the operands.

**Parameters:**

**instructions** (*collections.abc.Collection**[**UnparseableContentStreamInstructions**]*) – collection of instructions such as is returned
by [`parse_content_stream()`](#pikepdf.parse_content_stream)

**Returns:**
: 
A binary content stream, suitable for attaching to a Pdf.
To attach to a Pdf, use `Pdf.make_stream()`()`.

**Return type:**
: 
bytes

Changed in version 3.0: Now accept collections that contain any mixture of
`ContentStreamInstruction`, `ContentStreamInlineImage`, and the older
operand-operator tuples from pikepdf 2.x.

*class *pikepdf.models.ctm.MatrixStack(*initial_matrix=Matrix.identity()*)[](#pikepdf.models.ctm.MatrixStack)
: 
Tracks the CTM (current transformation matrix) in a PDF content stream.

The CTM starts as the initial matrix and can be changed via the ‘cm’
(concatenate matrix) operator –&gt; CTM = CTM x CM (with CTM and CM
being 3x3 matrixes). Initial matrix is the identity matrix unless overridden.

Furthermore can the CTM be stored to the stack via the ‘q’ operator.
This save the CTM and subsequent ‘cm’ operators change a copy of that CTM
–&gt; ‘q 1 0 0 1 0 0 cm’
–&gt; Copy CTM onto the stack and change the copy via ‘cm’

With the ‘Q’ operator the current CTM is replaced with the previous one from the
stack.

Error handling:
1. Popping from an empty stack results in CTM being set to the initial matrix
2. Multiplying with invalid operands sets the CTM to invalid
3. Multiplying an invalid CTM with a valid CM results in an invalid CTM
4. Stacking an invalid CTM results in a copy of that invalid CTM onto the stack
–&gt; All operations with an invalid CTM result in an invalid CTM
–&gt; The CTM is valid again when all invalid CTMs are popped off the stack

**Parameters:**

**initial_matrix** (*pikepdf._core.Matrix*)

pikepdf.models.ctm.get_objects_with_ctm(*page*, *initial_matrix=Matrix.identity()*)[](#pikepdf.models.ctm.get_objects_with_ctm)
: 
Determines the current transformation matrix (CTM) for each drawn object.

Filters objects with an invalid CTM.

**Parameters:**

- 
**page** (*pikepdf._core.Page*)

- 
**initial_matrix** (*pikepdf._core.Matrix*)

**Return type:**
: 
list[tuple[str, pikepdf._core.Matrix]]

## Content stream token filters[](#content-stream-token-filters)

*class *pikepdf.Token(*arg0*, *arg1*)[](#pikepdf.Token)
: 

**Parameters:**

- 
**arg0** ([*TokenType*](#pikepdf.TokenType))

- 
**arg1** (*bytes*)

*property *error_msg*: str*[](#pikepdf.Token.error_msg)
: 
If the token is an error, this returns the error message.

**Return type:**

str

*property *raw_value*: bytes*[](#pikepdf.Token.raw_value)
: 
The binary representation of a token.

**Return type:**

bytes

*property *type_*: [TokenType](#pikepdf.TokenType)*[](#pikepdf.Token.type_)
: 
Returns the type of token.

**Return type:**

[TokenType](#pikepdf.TokenType)

*property *value*: str*[](#pikepdf.Token.value)
: 
Interprets the token as a string.

**Return type:**

str

*class *pikepdf.TokenType(**args*, ***kwds*)[](#pikepdf.TokenType)
: 
Type of a token that appeared in a PDF content stream.

When filtering content streams, each token is labeled according to the role
in plays.

array_close*: int** = Ellipsis*[](#pikepdf.TokenType.array_close)

The token data represents the end of an array.

array_open*: int** = Ellipsis*[](#pikepdf.TokenType.array_open)
: 
The token data represents the start of an array.

bad*: int** = Ellipsis*[](#pikepdf.TokenType.bad)
: 
An invalid token.

bool*: int** = Ellipsis*[](#pikepdf.TokenType.bool)
: 
The token data represents an integer, real number, null or boolean,
respectively.

brace_close*: int** = Ellipsis*[](#pikepdf.TokenType.brace_close)
: 
The token data represents the end of a brace.

brace_open*: int** = Ellipsis*[](#pikepdf.TokenType.brace_open)
: 
The token data represents the start of a brace.

comment*: int** = Ellipsis*[](#pikepdf.TokenType.comment)
: 
Signifies a comment that appears in the content stream.

dict_close*: int** = Ellipsis*[](#pikepdf.TokenType.dict_close)
: 
The token data represents the end of a dictionary.

dict_open*: int** = Ellipsis*[](#pikepdf.TokenType.dict_open)
: 
The token data represents the start of a dictionary.

eof*: int** = Ellipsis*[](#pikepdf.TokenType.eof)
: 
Denotes the end of the tokens in this content stream.

inline_image*: int** = Ellipsis*[](#pikepdf.TokenType.inline_image)
: 
An inline image in the content stream. The whole inline image is
represented by the single token.

integer*: int** = Ellipsis*[](#pikepdf.TokenType.integer)
: 
The token data represents an integer.

name_*: int** = Ellipsis*[](#pikepdf.TokenType.name_)
: 
The token is the name (pikepdf.Name) of an object. In practice, these
are among the most interesting tokens.

Changed in version 3.0: In versions older than 3.0, `.name` was used instead. This interfered
with semantics of the `Enum` object, so this was fixed.

null*: int** = Ellipsis*[](#pikepdf.TokenType.null)
: 
The token data represents a null.

real*: int** = Ellipsis*[](#pikepdf.TokenType.real)
: 
The token data represents a real number.

space*: int** = Ellipsis*[](#pikepdf.TokenType.space)
: 
Whitespace within the content stream.

string*: int** = Ellipsis*[](#pikepdf.TokenType.string)
: 
The token data represents a string. The encoding is unclear and situational.

word*: int** = Ellipsis*[](#pikepdf.TokenType.word)
: 
Otherwise uncategorized bytes are returned as `word` tokens. PDF
operators are words.

*class *pikepdf.TokenFilter[](#pikepdf.TokenFilter)
: 

handle_token(*token=...*)[](#pikepdf.TokenFilter.handle_token)

Handle a [`pikepdf.Token`](#pikepdf.Token).

This is an abstract method that must be defined in a subclass
of `TokenFilter`. The method will be called for each token.
The implementation may return either `None` to discard the
token, the original token to include it, a new token, or an
iterable containing zero or more tokens. An implementation may
also buffer tokens and release them in groups (for example, it
could collect an entire PDF command with all of its operands,
and then return all of it).

The final token will always be a token of type `TokenType.eof`,
(unless an exception is raised).

If this method raises an exception, the exception will be
caught by C++, consumed, and replaced with a less informative
exception. Use [`pikepdf.Pdf.get_warnings()`](main.html#pikepdf.Pdf.get_warnings) to view the
original.

**Parameters:**

**token** ([*Token*](#pikepdf.Token))

**Return type:**
: 
None | [Token](#pikepdf.Token) | collections.abc.Iterable[[Token](#pikepdf.Token)]

---
# Overlays
Source: https://pikepdf.readthedocs.io/en/latest/topics/overlays.html

# Overlays, underlays, watermarks, n-up[](#overlays-underlays-watermarks-n-up)

You can use pikepdf to overlay pages or other content on top of other pages.

This might be used to do watermarks (typically an underlay, drawn before everything
else), n-up (compositing multiple individual pages on a large page, such as converting
slides from a presentation to 4-up for reading and printing).

If you are looking to merge pages from different PDFs, see [Merge (concatenate) PDF from several PDFs](pages.html#mergepdf).

In this example we use [`pikepdf.Page.add_overlay()`](../api/models.html#pikepdf.Page.add_overlay) to draw a thumbnail of
of the second page onto the first page.

```
&gt;&gt;&gt; from pikepdf import Pdf, Page, Rectangle

&gt;&gt;&gt; pdf = Pdf.open(...)

&gt;&gt;&gt; destination_page = Page(pdf.pages[0])

&gt;&gt;&gt; thumbnail = Page(pdf.pages[1])

&gt;&gt;&gt; destination_page.add_overlay(thumbnail, Rectangle(0, 0, 300, 300))

&gt;&gt;&gt; pdf.save(&quot;page1_with_page2_thumbnail.pdf&quot;)

```

The [`pikepdf.Rectangle`](../api/main.html#pikepdf.Rectangle) specifies the position on the target page into which
the other page can be drawn. The object will be drawn centered in a way that
fills as much space as possible while preserving aspect ratio.

Use [`pikepdf.Page.add_underlay()`](../api/models.html#pikepdf.Page.add_underlay) instead if you want content drawn underneath.
It is possible content drawn this way will be overdrawn by other objects.

Use [`pikepdf.Page.trimbox`](../api/models.html#pikepdf.Page.trimbox) to get a page’s dimensions.

`add_overlay` will copy content across `Pdf` objects as needed, and can copy
other pages or other Form XObjects.

`add_overlay` also preserves aspect ratio.
Use [`pikepdf.Page.as_form_xobject()`](../api/models.html#pikepdf.Page.as_form_xobject) and
[`pikepdf.Page.calc_form_xobject_placement()`](../api/models.html#pikepdf.Page.calc_form_xobject_placement) if you want more precise control
over placement.

Composition works using Form XObjects, which is how PDF captures of a group of
related objects for drawing. Some very basic PDF software may not support them,
or may fail to detect images contained within.

When perform n-up composition, it will work better to create your composition
within the existing document, rather than in a new document. Transforming the
existing document will ensure that metadata, annotations and hyperlinks are
preserved. For example, to convert 16 slides to 4×4-up pages for printing,
add four pages onto the end of the file, draw the slides onto the target pages,
and then delete the slides.

By default, `add_overlay` encapsulates the existing content stream in a way
that ensures the transformation matrix is first reset, since this behavior
aligns with user expectations. This adds a `q/Q` pair to (push/pop graphics
stack) to existing content streams. To disable this (usually desired) behavior
use `push_stack=False`.

---
# Encoding
Source: https://pikepdf.readthedocs.io/en/latest/topics/encoding.html

# Character encoding[](#character-encoding)

There are three hard problems in computer science:
1) Converting from PDF,
2) Converting to PDF, and
3) O̳̳̳̳̳̳̳̳̳̳̳̳̳̳̳̳̳Ҙ҉҉҉ʹʹ҉ʹ̨̨̨̨̨̨̨̨̃༃༃O̳̳̳̳̳̳̳̳̳̳̳̳̳̳̳̳̳Ҙ҉҉҉ʹʹ҉ʹ̨̨̨̨̨̨̨̨̃༃༃ʹʹ҉ʹ̨̨̨̨̨̨̨̨̃༃༃

—[Marseille Folog](https://twitter.com/fogus/status/1024657831084085248)

In most circumstances, pikepdf performs appropriate encodings and
decodings on its own, or returns [`pikepdf.String`](../api/main.html#pikepdf.String) if it is not clear
whether to present data as a string or binary data.

`str(pikepdf.String)` is performed by inspecting the binary data. If the
binary data begins with a UTF-16 byte order mark, then the data is
interpreted as UTF-16 and returned as a Python `str`. Otherwise, the data
is returned as a Python `str`, if the binary data will be interpreted as
PDFDocEncoding and decoded to `str`. Again, in most cases this is correct
behavior and will operate transparently.

Some functions are available in circumstances where it is necessary to force
a particular conversion.

## PDFDocEncoding[](#pdfdocencoding)

The PDF specification defines PDFDocEncoding, a character encoding used only
in PDFs. This encoding matches ASCII for code points 32 through 126 (0x20 to
0x7e). At all other code points, it is not ASCII and cannot be treated as
equivalent. If you look at a PDF in a binary file viewer (hex editor), a string
surrounded by parentheses such as `(Hello World)` is usually using
PDFDocEncoding.

When pikepdf is imported, it automatically registers `&quot;pdfdoc&quot;` as a codec
with the standard library, so that it may be used in string and byte
conversions.

```
&quot;•&quot;.encode(&#39;pdfdoc&#39;) == b&#39;\x81&#39;

```

Other Python PDF libraries may register their own `pdfdoc` codecs. Unfortunately,
the order of imports will determine which codec “wins” and gets mapped
to the `'pdfdoc'` string. Fortunately, these implementations should be
quite compatible with each other anyway since they do the same things.

pikepdf also registers `'pdfdoc_pikepdf'`, if you want to ensure use of
pikepdf’s codec, i.e. `s.encode('pdfdoc_pikepdf')`.

Changed in version 5.0.0: Some issues with the conversion of obscure characters in PDFDocEncoding were fixed. Older versions of pikepdf may not convert PDFDocEncoding in all cases.

---
# Installation
Source: https://pikepdf.readthedocs.io/en/latest/installation.html

# Installation[](#installation)

## Basic installation[](#basic-installation)

Most users on Linux, macOS or Windows with x64 systems should use `pip` to
install pikepdf in their current Python environment (such as your project’s
virtual environment).

```
pip install pikepdf

```

Use `pip install --user pikepdf` to install the package for the current user
only. Use `pip install pikepdf` to install to a virtual environment.

## Binary wheel availability[](#binary-wheel-availability)

Python binary wheel availability[](#id1)

3.9

3.10

3.11

3.12

3.13

 macOS Intel

✅

✅

✅

✅

✅

 macOS Apple Silicon

✅

✅

✅

✅

✅

 Windows x64

✅

✅

✅

✅

✅

 manylinux2014 x64

✅

✅

✅

✅

✅

 manylinux2014 aarch64 (ARM64)

✅

✅

✅

✅

✅

 musllinux x64

✅

✅

✅

✅

✅

 musllinux aarch64 (ARM64)

✅

✅

✅

✅

✅

- 
✅ wheels are available

- 
❌ wheels are not likely to be produced for this platform and Python version

- 
⏳ we are waiting on a third party to implement better support for this configuration

- 
⚠️ wheel is released but cannot be tested - use with caution

Binary wheels should work on most systems, provided a recent version
of pip is used to install them. Old versions of pip, especially before 20.0,
may fail to check appropriate versions.

macOS 14 or newer is typically required for binary wheels. Older versions may
work if compiled from source.

Windows 7 or newer is required. Windows wheels include a recent copy of libqpdf.

Most Linux distributions support manylinux2014, with the notable except of
[Alpine Linux], and older Linux distributions that do not have C++20-capable
compilers. The Linux wheels include recent copies of libqpdf, libjpeg, and zlib.

Source builds are usually possible where binary wheels are available.

## Platform support[](#platform-support)

Some platforms include versions of pikepdf that are distributed by the system
package manager (such as `apt`). These versions may lag behind the version
distributed with PyPI, but may be convenient for users that cannot use binary
wheels.

Packaged fish.[](#id2)

### Debian, Ubuntu and other APT-based distributions[](#debian-ubuntu-and-other-apt-based-distributions)

```
apt install pikepdf

```

---
# Pagelayout
Source: https://pikepdf.readthedocs.io/en/latest/topics/pagelayout.html

# Default appearance in PDF viewers[](#default-appearance-in-pdf-viewers)

Using pikepdf you can control the initial page layout and page mode, that is,
how a PDF will appear by default when loaded in a PDF viewer.

These settings are changed written to the PDF’s Root object. Note that the PDF
viewer may ignore them and user preferences may override, etc.

```
from pikepdf import Pdf, Dictionary, Name
with Pdf.open(&#39;input.pdf&#39;) as pdf:
    pdf.Root.PageLayout = Name.SinglePage
    pdf.Root.PageMode = Name.FullScreen
    pdf.save(&#39;output.pdf&#39;)

```

For reference, the tables below provide summarize the available options.

PageLayout definitions[](#id1)

Value

Meaning

Name.SinglePage

Display one page at a time (default)

Name.OneColumn

Display the pages in one column

Name.TwoColumnLeft

Display the pages in two columns, with odd-numbered pages on the left

Name.TwoColumnRight

Display the pages in two columns, with odd-numbered pages on the right

Name.TwoPageLeft

Display the pages two at a time, with odd-numbered pages on the left

Name.TwoPageRight

Display the pages two at a time, with odd-numbered pages on the right

PageMode definitions[](#id2)

Value

Meaning

Name.UseNone

Neither document outline nor thumbnail images visible (default)

Name.UseOutlines

Document outline visible

Name.UseThumbs

Thumbnail images visible

Name.FullScreen

Full-screen mode, with no menu bar, window controls, or any other window visible

Name.UseOC

Optional content group panel visible

Name.UseAttachments

Attachments panel visible

---
# Canvas
Source: https://pikepdf.readthedocs.io/en/latest/api/canvas.html

# Canvas[](#canvas)

The `pikepdf.canvas` provides a low-level PDF rendering API.

*class *pikepdf.canvas.Canvas(***, *page_size*)[](#pikepdf.canvas.Canvas)
: 
Canvas for rendering PDFs with pikepdf.

All drawing is done on a pikepdf canvas using the `.do` property.
This interface manages the graphics state of the canvas.

A Canvas can be exported as a single page Pdf using `.to_pdf`. This Pdf can
then be merged into other PDFs or written to a file.

**Parameters:**

**page_size** (*tuple**[**int** | **float**, **int** | **float**]*)

add_font(*resource_name*, *font*)[](#pikepdf.canvas.Canvas.add_font)
: 
Add a font to the page.

**Parameters:**

- 
**resource_name** (*pikepdf.objects.Name*)

- 
**font** ([*Font*](#pikepdf.canvas.Font))

*property *do*: [_CanvasAccessor](#pikepdf.canvas._CanvasAccessor)*[](#pikepdf.canvas.Canvas.do)
: 
Do operations on the current graphics state.

**Return type:**

[_CanvasAccessor](#pikepdf.canvas._CanvasAccessor)

page_size[](#pikepdf.canvas.Canvas.page_size)
: 

to_pdf()[](#pikepdf.canvas.Canvas.to_pdf)
: 
Render the canvas as a single page PDF.

**Return type:**

pikepdf._core.Pdf

*class *pikepdf.canvas._CanvasAccessor(*cs*, *images=None*)[](#pikepdf.canvas._CanvasAccessor)
: 
Contains all drawing methods class for drawing on a Canvas.

**Parameters:**

**cs** ([*ContentStreamBuilder*](#pikepdf.canvas.ContentStreamBuilder))

cm(*matrix*)[](#pikepdf.canvas._CanvasAccessor.cm)
: 
Concatenate a new transformation matrix to the current matrix.

**Parameters:**

**matrix** (*pikepdf._core.Matrix*)

dashes(**args*)[](#pikepdf.canvas._CanvasAccessor.dashes)
: 
Set dashes.

draw_image(*image*, *x*, *y*, *width*, *height*)[](#pikepdf.canvas._CanvasAccessor.draw_image)
: 
Draw image at (x,y) with width w and height h.

**Parameters:**

**image** (*pathlib.Path** | **str** | **PIL.Image.Image*)

draw_text(*text*)[](#pikepdf.canvas._CanvasAccessor.draw_text)
: 
Draw text object.

**Parameters:**

**text** ([*Text*](#pikepdf.canvas.Text))

fill_color(*color*)[](#pikepdf.canvas._CanvasAccessor.fill_color)
: 
Set fill color.

**Parameters:**

**color** (*Color*)

line(*x1*, *y1*, *x2*, *y2*)[](#pikepdf.canvas._CanvasAccessor.line)
: 
Draw line from (x1,y1) to (x2,y2).

line_width(*width*)[](#pikepdf.canvas._CanvasAccessor.line_width)
: 
Set line width.

pop()[](#pikepdf.canvas._CanvasAccessor.pop)
: 
Restore the previous graphics state.

push()[](#pikepdf.canvas._CanvasAccessor.push)
: 
Save the graphics state.

rect(*x*, *y*, *w*, *h*, *fill*)[](#pikepdf.canvas._CanvasAccessor.rect)
: 
Draw optionally filled rectangle at (x,y) with width w and height h.

**Parameters:**

**fill** (*bool*)

save_state(***, *cm=None*)[](#pikepdf.canvas._CanvasAccessor.save_state)
: 
Save the graphics state and restore it on exit.

Optionally, concatenate a transformation matrix. Implements
the commonly used pattern of:

q cm … Q

**Parameters:**

**cm** (*pikepdf._core.Matrix** | **None*)

stroke_color(*color*)[](#pikepdf.canvas._CanvasAccessor.stroke_color)
: 
Set stroke color.

**Parameters:**

**color** (*Color*)

*class *pikepdf.canvas.ContentStreamBuilder[](#pikepdf.canvas.ContentStreamBuilder)
: 
Content stream builder.

append_rectangle(*x*, *y*, *w*, *h*)[](#pikepdf.canvas.ContentStreamBuilder.append_rectangle)

Append rectangle to path.

**Parameters:**

- 
**x** (*float*)

- 
**y** (*float*)

- 
**w** (*float*)

- 
**h** (*float*)

begin_marked_content(*mctype*)[](#pikepdf.canvas.ContentStreamBuilder.begin_marked_content)
: 
Begin marked content sequence.

**Parameters:**

**mctype** (*pikepdf.objects.Name*)

begin_marked_content_proplist(*mctype*, *mcid*)[](#pikepdf.canvas.ContentStreamBuilder.begin_marked_content_proplist)
: 
Begin marked content sequence.

**Parameters:**

- 
**mctype** (*pikepdf.objects.Name*)

- 
**mcid** (*int*)

begin_text()[](#pikepdf.canvas.ContentStreamBuilder.begin_text)
: 
Begin text object.

All text operations must be contained within a text object, and are invalid
otherwise. The text matrix and font are reset for each text object. Text objects
may not be nested.

build()[](#pikepdf.canvas.ContentStreamBuilder.build)
: 
Build content stream.

**Return type:**

bytes

cm(*matrix*)[](#pikepdf.canvas.ContentStreamBuilder.cm)
: 
Concatenate matrix.

**Parameters:**

**matrix** (*pikepdf._core.Matrix*)

draw_xobject(*name*)[](#pikepdf.canvas.ContentStreamBuilder.draw_xobject)
: 
Draw XObject.

Add instructions to render an XObject. The XObject must be
defined in the document.

**Parameters:**

**name** (*pikepdf.objects.Name*) – Name of XObject

end_marked_content()[](#pikepdf.canvas.ContentStreamBuilder.end_marked_content)
: 
End marked content sequence.

end_text()[](#pikepdf.canvas.ContentStreamBuilder.end_text)
: 
End text object.

extend(*other*)[](#pikepdf.canvas.ContentStreamBuilder.extend)
: 
Append another content stream.

**Parameters:**

**other** ([*ContentStreamBuilder*](#pikepdf.canvas.ContentStreamBuilder)* | **bytes*)

fill()[](#pikepdf.canvas.ContentStreamBuilder.fill)
: 
Stroke and close path.

line(*x1*, *y1*, *x2*, *y2*)[](#pikepdf.canvas.ContentStreamBuilder.line)
: 
Draw line.

**Parameters:**

- 
**x1** (*float*)

- 
**y1** (*float*)

- 
**x2** (*float*)

- 
**y2** (*float*)

move_cursor(*dx*, *dy*)[](#pikepdf.canvas.ContentStreamBuilder.move_cursor)
: 
Move cursor by the given offset, relative to the start of the current line.

This operator modifies the both current text matrix and the text line matrix.
This means that, in addition to moving the current cursor, the new cursor will
also be defined as the start of a new line.

The new position will be redefined as the new start of the line even if the y
offset is 0; what to a user may look like a single line of text could be encoded
in the PDF content stream as multiple “lines”. It’s not uncommon for PDFs to be
written with every word as a separate “line”, allowing the PDF writer to
explicitly define the spacing between each word.

move_cursor_new_line()[](#pikepdf.canvas.ContentStreamBuilder.move_cursor_new_line)
: 
Move cursor to the start of the next line.

This moves down by the current leading value, and resets the x position back to
the value it had at the beginning of the current line.

This operator modifies the both current text matrix and the text line matrix.
This means that, in addition to moving the current cursor, the new cursor will
also be defined as the start of a new line.

The value this operation moves the cursor is set using `set_text_leading`.

pop()[](#pikepdf.canvas.ContentStreamBuilder.pop)
: 
Restore the graphics state.

push()[](#pikepdf.canvas.ContentStreamBuilder.push)
: 
Save the graphics state.

set_dashes(*array=None*, *phase=0*)[](#pikepdf.canvas.ContentStreamBuilder.set_dashes)
: 
Set dashes.

set_fill_color(*r*, *g*, *b*)[](#pikepdf.canvas.ContentStreamBuilder.set_fill_color)
: 
Set RGB fill color.

**Parameters:**

- 
**r** (*float*)

- 
**g** (*float*)

- 
**b** (*float*)

set_line_width(*width*)[](#pikepdf.canvas.ContentStreamBuilder.set_line_width)
: 
Set line width.

set_stroke_color(*r*, *g*, *b*)[](#pikepdf.canvas.ContentStreamBuilder.set_stroke_color)
: 
Set RGB stroke color.

**Parameters:**

- 
**r** (*float*)

- 
**g** (*float*)

- 
**b** (*float*)

set_text_char_spacing(*size*)[](#pikepdf.canvas.ContentStreamBuilder.set_text_char_spacing)
: 
Set the character spacing (Tc) for future text operations.

This is a value, measured in unscaled text-space units, which will be used to
adjust the spacing between characters. A value of 0 (the default) means that,
for each rendered glyph, the cursor will advance only the actual width of the
glyph. Positive values will result in additional space between characters, and
negative values will cause glyphs to overlap.

In vertical writing, the sign works opposite of what one might expect: a
positive value shrinks the space, and a negative value increases it.

**Parameters:**

**size** (*int** | **float** | **decimal.Decimal*)

set_text_font(*font*, *size*)[](#pikepdf.canvas.ContentStreamBuilder.set_text_font)
: 
Set text font and size.

This operator is mandatory in order to show text. Any text object which attempts
to show text without first calling this operator is invalid.

The font name must match an entry in the current resources dictionary. The font
size is expressed in text-space units. Assuming no text scaling is in place, and
the PDF has not set a user-defined unit in the page dictionary, then text space
units will be points (defined as 1/72 of an inch).

**Parameters:**

- 
**font** (*pikepdf.objects.Name*)

- 
**size** (*int** | **float** | **decimal.Decimal*)

set_text_horizontal_scaling(*scale*)[](#pikepdf.canvas.ContentStreamBuilder.set_text_horizontal_scaling)
: 
Set text horizontal scaling.

**Parameters:**

**scale** (*float*)

set_text_leading(*size*)[](#pikepdf.canvas.ContentStreamBuilder.set_text_leading)
: 
Set the leading value (TL) for future text operations.

This is the vertical spacing between lines. Specifically, it is defined as the
distance between the baseline of the previous line to the baseline of the next
line.

**Parameters:**

**size** (*int** | **float** | **decimal.Decimal*)

set_text_matrix(*matrix*)[](#pikepdf.canvas.ContentStreamBuilder.set_text_matrix)
: 
Set text matrix.

The text matrix defines the conversion between text-space and page-space, in
terms of both scaling and translation. If this matrix scales the text, then
it redefines text-space units as being some scale factor of page-space units.

**Parameters:**

**matrix** (*pikepdf._core.Matrix*)

set_text_rendering(*mode*)[](#pikepdf.canvas.ContentStreamBuilder.set_text_rendering)
: 
Set text rendering mode.

**Parameters:**

**mode** (*int*)

set_text_word_spacing(*size*)[](#pikepdf.canvas.ContentStreamBuilder.set_text_word_spacing)
: 
Set the word spacing (Tw) for future text operations.

This is a value, measured in unscaled text-space units, which will be added to
the width of any ASCII space characters.

In vertical writing, the sign works opposite of what one might expect: a
positive value shrinks the space, and a negative value increases it.

**Parameters:**

**size** (*int** | **float** | **decimal.Decimal*)

show_text(*encoded*)[](#pikepdf.canvas.ContentStreamBuilder.show_text)
: 
Show text.

The text must be encoded in character codes expected by the font.

**Parameters:**

**encoded** (*bytes*)

show_text_line(*encoded*)[](#pikepdf.canvas.ContentStreamBuilder.show_text_line)
: 
Advance to the next line and show text.

The text must be encoded in character codes expected by the font.

This is functionally equivalent to `move_cursor_new_line()` followed by
`show_text_string(encoded)`, but in a single operation.

**Parameters:**

**encoded** (*bytes*)

show_text_line_with_spacing(*encoded*, *word_spacing*, *char_spacing*)[](#pikepdf.canvas.ContentStreamBuilder.show_text_line_with_spacing)
: 
Advance to the next line and show text.

The text must be encoded in character codes expected by the font.

This is functionally equivalent to `set_text_char_spacing(char_spacing)` and
`set_text_word_spacing()`, followed by `move_cursor_new_line()` and then
`show_text(encoded)`, all in a single operation.

**Parameters:**

- 
**encoded** (*bytes*)

- 
**word_spacing** (*int*)

- 
**char_spacing** (*int*)

show_text_with_kerning(**parts*)[](#pikepdf.canvas.ContentStreamBuilder.show_text_with_kerning)
: 
Show text, with manual spacing (kerning) options.

Arguments are either bytes, which represent the actual text to show, or numbers,
which move the cursor. The units for the numbers are expressed in thousandths
of a text-space unit (thus typically equivalent to a glyph-space unit).

For horizontal writing, positive values move the cursor left, and negative
right. For vertical writing, positive values move down and negative up.

The text must be encoded in character codes expected by the font.

**Parameters:**

**parts** (*bytes** | **int** | **float** | **decimal.Decimal*)

stroke_and_close()[](#pikepdf.canvas.ContentStreamBuilder.stroke_and_close)
: 
Stroke and close path.

*class *pikepdf.canvas.LoadedImage[](#pikepdf.canvas.LoadedImage)
: 
Loaded image.

This class is used to track images that have been loaded into a
canvas.

image*: PIL.Image.Image*[](#pikepdf.canvas.LoadedImage.image)

name*: pikepdf.objects.Name*[](#pikepdf.canvas.LoadedImage.name)
: 

## Text and fonts[](#text-and-fonts)

*class *pikepdf.canvas.Text(*direction=TextDirection.LTR*)[](#pikepdf.canvas.Text)
: 
Text object for rendering text on a pikepdf canvas.

font(*font*, *size*)[](#pikepdf.canvas.Text.font)

Set font and size.

**Parameters:**

- 
**font** (*pikepdf.objects.Name*)

- 
**size** (*float*)

horiz_scale(*scale*)[](#pikepdf.canvas.Text.horiz_scale)
: 
Set text horizontal scaling.

move_cursor(*x*, *y*)[](#pikepdf.canvas.Text.move_cursor)
: 
Move cursor.

render_mode(*mode*)[](#pikepdf.canvas.Text.render_mode)
: 
Set text rendering mode.

show(*text*)[](#pikepdf.canvas.Text.show)
: 
Show text.

The text must be encoded in character codes expected by the font.
If a text string is passed, it will be encoded as UTF-16BE.
Text rendering will not work properly if the font’s character
codes are not consistent with UTF-16BE. This is a rudimentary
interface. You’ve been warned.

**Parameters:**

**text** (*str** | **bytes*)

text_transform(*matrix*)[](#pikepdf.canvas.Text.text_transform)
: 
Set text matrix.

**Parameters:**

**matrix** (*pikepdf._core.Matrix*)

*class *pikepdf.canvas.TextDirection(**args*, ***kwds*)[](#pikepdf.canvas.TextDirection)
: 
Enumeration for text direction.

LTR* = 1*[](#pikepdf.canvas.TextDirection.LTR)

Left to right, the default.

RTL* = 2*[](#pikepdf.canvas.TextDirection.RTL)
: 
Right to left, Arabic, Hebrew, Persian, etc.

*class *pikepdf.canvas.Font[](#pikepdf.canvas.Font)
: 
Base class for fonts.

*abstractmethod *register(*pdf*)[](#pikepdf.canvas.Font.register)

Register the font.

Create several data structures in the Pdf to describe the font.

After registering the font, the returned object should be added to the
/Resources dictionary of any page or Form XObject that uses the font. For
example one might write:

`python
page.Resources.Font[Name.Arial] = font.register(pdf)
`

The same object can be used for multiple pages or Form XObjects, since it is
an indirect object.

Returns a Dictionary suitable for insertion into a /Resources /Font dictionary.

**Parameters:**

**pdf** (*pikepdf._core.Pdf*)

**Return type:**
: 
pikepdf.objects.Dictionary

*abstractmethod *text_width(*text*, *fontsize*)[](#pikepdf.canvas.Font.text_width)
: 
Estimate the width of a text string when rendered with the given font.

**Parameters:**

- 
**text** (*str** | **bytes*)

- 
**fontsize** (*float** | **int** | **decimal.Decimal*)

**Return type:**
: 
float | int | decimal.Decimal

*class *pikepdf.canvas.Helvetica[](#pikepdf.canvas.Helvetica)
: 
Helvetica font.

Helvetica is one of the 14 PDF standard fonts that can typically be counted on being
present even if not embedded in the PDF document. However, starting with PDF 2.0,
PDF processors are no longer guaranteed to have these fonts. See 9.6.2.2.

register(*pdf*)[](#pikepdf.canvas.Helvetica.register)

Register the font.

**Parameters:**

**pdf** (*pikepdf._core.Pdf*)

**Return type:**
: 
pikepdf.objects.Dictionary

*abstractmethod *text_width(*text*, *fontsize*)[](#pikepdf.canvas.Helvetica.text_width)
: 
Estimate the width of a text string when rendered with the given font.

**Parameters:**

- 
**text** (*str** | **bytes*)

- 
**fontsize** (*float** | **int** | **decimal.Decimal*)

**Return type:**
: 
float | int | decimal.Decimal

*class *pikepdf.canvas.SimpleFont(*data*)[](#pikepdf.canvas.SimpleFont)
: 
Font implementation designed to work with Type 1 Fonts and TrueType fonts.

As described in section 9.6 of the PDF spec.

See also section 9.8: Font Descriptors.

The PDF spec also considers Type3 fonts to be “Simple Fonts”, but Type3 fonts are
not implemented here.

**Parameters:**

**data** (*pikepdf.objects.Dictionary*)

*property *ascent*: decimal.Decimal*[](#pikepdf.canvas.SimpleFont.ascent)
: 
Returns ascent for a SimpleFont.

**Return type:**

decimal.Decimal

convert_width(*width*, *fontsize=1*)[](#pikepdf.canvas.SimpleFont.convert_width)
: 
Convert width from glyph space to text space, scaling by font size.

Scaling based on the nominal height (see 9.2.2):

“This standard is arranged so that the nominal height of tightly spaced lines of
text is 1 unit. … The standard-size font shall then be scaled to be usable.”

This means, essentially, that a font size of 1 means a character is 1 text-space
unit high, and a font size of 12 is 12 text-space units high. Assuming no text
scaling is in place (such as via the text matrix), and the PDF has not set a
user-defined unit in the page dictionary, then text space units will be points
(defined as 1/72 of an inch).

**Parameters:**

- 
**width** (*int** | **decimal.Decimal*)

- 
**fontsize** (*int** | **decimal.Decimal*)

**Return type:**
: 
int | decimal.Decimal

convert_width_reverse(*width*, *fontsize=1*)[](#pikepdf.canvas.SimpleFont.convert_width_reverse)
: 
Convert width from text space back to glyph space, scaling by font size.

**Parameters:**

- 
**width** (*int** | **decimal.Decimal*)

- 
**fontsize** (*int** | **decimal.Decimal*)

**Return type:**
: 
int | decimal.Decimal

data*: pikepdf.objects.Dictionary*[](#pikepdf.canvas.SimpleFont.data)
: 

*property *descent*: decimal.Decimal*[](#pikepdf.canvas.SimpleFont.descent)
: 
Returns descent for a SimpleFont.

**Return type:**

decimal.Decimal

encode(*text*)[](#pikepdf.canvas.SimpleFont.encode)
: 
Encode a string in the encoding used by this font.

This currently only works with fonts that use the WinAnsiEncoding or the
MacRomanEncoding. Differences maps are supported, though with a limited
set of recognized character names.

**Parameters:**

**text** (*str*)

**Return type:**
: 
bytes

*property *leading*: int | decimal.Decimal*[](#pikepdf.canvas.SimpleFont.leading)
: 
Returns leading for a SimpleFont.

**Return type:**

int | decimal.Decimal

*classmethod *load(*name*, *resource_dict*)[](#pikepdf.canvas.SimpleFont.load)
: 
Load a font from the specified resource dictionary.

**Parameters:**

- 
**name** (*pikepdf.objects.Name*)

- 
**resource_dict** (*pikepdf.objects.Dictionary*)

**Return type:**
: 
[SimpleFont](#pikepdf.canvas.SimpleFont)

register(*pdf*)[](#pikepdf.canvas.SimpleFont.register)
: 
Register the font.

**Parameters:**

**pdf** (*pikepdf._core.Pdf*)

**Return type:**
: 
pikepdf.objects.Dictionary

text_width(*text*, *fontsize=1*, ***, *char_spacing=0*, *word_spacing=0*)[](#pikepdf.canvas.SimpleFont.text_width)
: 
Get the width of the string.

This is the width of the string when rendered with the current font, scaled by
the given font size.

**Parameters:**

- 
**text** (*str** | **bytes*) – The string to check

- 
**fontsize** (*int** | **decimal.Decimal*) – The target font size in text-space units. (Assuming text space
isn’t being scaled, this means the font size in points.)

- 
**char_spacing** (*int** | **decimal.Decimal*) – Additional space that will be added between each character.
May be negative.

- 
**word_spacing** (*int** | **decimal.Decimal*) – Additional space that will be added after each ASCII space
character (’ ‘). May be negative.

**Return type:**
: 
int | decimal.Decimal

unscaled_char_width(*char*)[](#pikepdf.canvas.SimpleFont.unscaled_char_width)
: 
Get the (unscaled) width of the character, in glyph-space units.

**Parameters:**

**char** (*int** | **bytes** | **str*) – The character to check. May be a char code, or a string containing a
single character.

**Return type:**
: 
decimal.Decimal

---
# Source Build
Source: https://pikepdf.readthedocs.io/en/latest/source_build.html

# Building from source[](#building-from-source)

If you are a developer and you want to build from source, follow these steps.

## Requirements[](#requirements)

pikepdf requires:

- 
a C++20 compliant compiler

- 
[pybind11](https://github.com/pybind/pybind11)

- 
libqpdf 11.9.0 or higher from the
[qpdf](https://qpdf.org) project.

On Linux the library and headers for libqpdf must be installed because pikepdf
compiles code against it and links to it.

Check [Repology for qpdf](https://repology.org/project/qpdf/badges) to
see if a recent version of qpdf is available for your platform. Otherwise you
must
[build qpdf from source](https://github.com/qpdf/qpdf?tab=readme-ov-file#building-from-source-distribution-on-unixlinux).
(Consider using the binary wheels, which bundle the required version of
libqpdf.)

Note

pikepdf should be built with the same compiler and linker as libqpdf; to be
precise both **must** use the same C++ ABI. On some platforms, setup.py may
not pick the correct compiler so one may need to set environment variables
`CC` and `CXX` to redirect it. If the wrong compiler is selected,
`import pikepdf._core` will throw an `ImportError` about a missing
symbol.

---
# Exceptions
Source: https://pikepdf.readthedocs.io/en/latest/api/exceptions.html

# Exceptions[](#exceptions)

*exception *pikepdf.exceptions.PdfError[](#pikepdf.exceptions.PdfError)
: 
General pikepdf-specific exception.

*exception *pikepdf.exceptions.PasswordError[](#pikepdf.exceptions.PasswordError)
: 
Exception thrown when the supplied password is incorrect.

*exception *pikepdf.exceptions.ForeignObjectError[](#pikepdf.exceptions.ForeignObjectError)
: 
When a complex object is copied into a foreign PDF without proper methods.

Use `Pdf.copy_foreign()`.

*exception *pikepdf.exceptions.OutlineStructureError[](#pikepdf.exceptions.OutlineStructureError)
: 
Indicates an error in the outline data structure.

*exception *pikepdf.exceptions.UnsupportedImageTypeError[](#pikepdf.exceptions.UnsupportedImageTypeError)
: 
This image is formatted in a way pikepdf does not supported.

*exception *pikepdf.exceptions.HifiPrintImageNotTranscodableError[](#pikepdf.exceptions.HifiPrintImageNotTranscodableError)
: 
Image contains high fidelity printing information and cannot be extracted.

*exception *pikepdf.exceptions.InvalidPdfImageError[](#pikepdf.exceptions.InvalidPdfImageError)
: 
This image is not valid according to the PDF 1.7 specification.

*exception *pikepdf.exceptions.DataDecodingError[](#pikepdf.exceptions.DataDecodingError)
: 
Exception thrown when a stream object in a PDF cannot be decoded.

*exception *pikepdf.exceptions.DeletedObjectError[](#pikepdf.exceptions.DeletedObjectError)
: 
When a required object is accessed after deletion.

Thrown when accessing a `Object` that relies on a `Pdf`
that was deleted using the Python `delete` statement or collected by the
Python garbage collector. To resolve this error, you must retain a reference
to the Pdf for the whole time you may be accessing it.

Added in version 7.0.

*exception *pikepdf.exceptions.DependencyError[](#pikepdf.exceptions.DependencyError)
: 
A third party dependency is needed to extract streams of this type.

*exception *pikepdf.exceptions.PdfParsingError(*message=None*, *line=None*)[](#pikepdf.exceptions.PdfParsingError)
: 
Error when parsing a PDF content stream.

*exception *pikepdf.exceptions.ImageDecompressionError[](#pikepdf.exceptions.ImageDecompressionError)
: 
Image decompression error.

---
# Streams
Source: https://pikepdf.readthedocs.io/en/latest/topics/streams.html

# Stream objects[](#stream-objects)

A [`pikepdf.Stream`](../api/main.html#pikepdf.Stream) object works like a PDF dictionary with some encoded
bytes attached. The dictionary is metadata that describes how the stream is
encoded. PDF can, and regularly does, use a variety of encoding filters. A
stream can be encoded with one or more filters. Images are a type of stream
object.

This is not the same type of object as Python’s file-like I/O objects, which are
sometimes called streams.

Most of the interesting content in a PDF (images and content streams) are
inside stream objects.

Because the PDF specification unfortunately defines several terms that involve the
word *stream*, let’s attempt to clarify:

When it comes to taxonomy, software developers have it easy.[](#id1)

**stream object**: 
A PDF object that contains binary data and a metadata dictionary that describes
it, represented as [`pikepdf.Stream`](../api/main.html#pikepdf.Stream), a subclass of [`pikepdf.Object`](../api/main.html#pikepdf.Object).
In HTML this is equivalent to a `&lt;object&gt;` tag with attributes and data.

**object stream**: 
A stream object (not a typo, an object stream really is a type of stream
object) in a PDF that contains a number of other objects in a
PDF, grouped together for better compression. In pikepdf there is an option
to save PDFs with this feature enabled to improve compression. Otherwise,
this is just a detail about how PDF files are encoded. When object streams
are present, pikepdf automatically decompresses them as necessary; no special
steps are needed to access a PDF that contains object streams.

**content stream**: 
A stream object that contains some instructions to draw graphics
and text on a page, or inside a Form XObject, and in some other situations.
In HTML this is equivalent to the HTML file itself. Content streams only draw
one page (or canvas, for a Form XObject). Each page needs its own content stream
to draw its contents.

**Form XObject**: 
A group of images, text and drawing commands that can be rendered elsewhere
in a PDF as a group. This is often used when a group of objects are needed
at different scales or on multiple pages. In HTML this is like an `&lt;svg&gt;`.
It is not a fillable PDF form (although a fillable PDF form could involve
Form XObjects).

**(Python) stream**: 
A stream is another name for a file object or file-like object, as described
in the Python `io` module.

## Reading stream objects[](#reading-stream-objects)

Fortunately, `pikepdf.Stream.read_bytes()` will apply all filters
and decode the uncompressed bytes, or throw an error if this is not possible.
`pikepdf.Stream.read_raw_bytes()` provides access to the compressed bytes.

Three types of stream object are particularly noteworthy: content streams,
which describe the order of drawing operators; images; and XMP metadata.
pikepdf provides helper functions for working with these types of streams.

## Reading stream objects as a Python I/O streams[](#reading-stream-objects-as-a-python-i-o-streams)

You were warned about terminology.

To preserve our remaining sanity, you cannot access a
stream object as a file-like object directly.

To efficiently access a `pikepdf.Stream` as a Python file object, you may do:

```
pdf.pages[0].Contents.page_contents_coalesce()
filelike_object = BytesIO(pdf.pages[0].Contents.get_stream_buffer())

```

---
# Objects
Source: https://pikepdf.readthedocs.io/en/latest/topics/objects.html

# Object model[](#object-model)

This section covers the object model pikepdf uses in more detail.

A [`pikepdf.Object`](../api/main.html#pikepdf.Object) is a Python wrapper around a C++ `QPDFObjectHandle`
which, as the name suggests, is a handle (or pointer) to a data structure in
memory, or possibly a reference to data that exists in a file. Importantly, an
object can be a scalar quantity (like a string) or a compound quantity (like a
list or dict, that contains other objects). The fact that the C++ class involved
here is an object *handle* is an implementation detail; it shouldn’t matter for
a pikepdf user.

The simplest types in PDFs are directly represented as Python types: `int`,
`bool`, and `None` stand for PDF integers, booleans and the “null”.
`Decimal` is used for floating point numbers in PDFs. If a
value in a PDF is assigned a Python `float`, pikepdf will convert it to
`Decimal`.

Types that are not directly convertible to Python are represented as
[`pikepdf.Object`](../api/main.html#pikepdf.Object), a compound object that offers a superset of possible
methods, some of which only if the underlying type is suitable. Use the
EAFP idiom, or
`isinstance` to determine the type more precisely. This partly reflects the
fact that the PDF specification allows many data fields to be one of several
types.

For convenience, the `repr()` of a `pikepdf.Object` will display a
Python expression that replicates the existing object (when possible), so it
will say:

```
&gt;&gt;&gt; catalog_name = pdf.Root.Type
pikepdf.Name(&quot;/Catalog&quot;)
&gt;&gt;&gt; isinstance(catalog_name, pikepdf.Name)
True
&gt;&gt;&gt; isinstance(catalog_name, pikepdf.Object)
True

```

## Making PDF objects[](#making-pdf-objects)

You may construct a new object with one of the classes:

- 
[`pikepdf.Array`](../api/main.html#pikepdf.Array)

- 
[`pikepdf.Dictionary`](../api/main.html#pikepdf.Dictionary)

- 
[`pikepdf.Name`](../api/main.html#pikepdf.Name) - the type used for keys in PDF Dictionary objects

- 
[`pikepdf.String`](../api/main.html#pikepdf.String) - a text string
(treated as `bytes` and `str` depending on context)

These may be thought of as subclasses of `pikepdf.Object`. (Internally they
**are** `pikepdf.Object`.)

There are a few other classes for special PDF objects that don’t
map to Python as neatly.

- 
`pikepdf.Operator` - a special object involved in processing content
streams

- 
`pikepdf.Stream` - a special object similar to a `Dictionary` with
binary data attached

- 
`pikepdf.InlineImage` - an image that is embedded in content streams

The great news is that it’s often unnecessary to construct `pikepdf.Object`
objects when working with pikepdf. Python types are transparently *converted* to
the appropriate pikepdf object when passed to pikepdf APIs – when possible.
However, pikepdf sends `pikepdf.Object` types back to Python on return calls,
in most cases, because pikepdf needs to keep track of objects that came from
PDFs originally.

## Object lifecycle and memory management[](#object-lifecycle-and-memory-management)

As mentioned above, a [`pikepdf.Object`](../api/main.html#pikepdf.Object) may reference data that is lazily
loaded from its source [`pikepdf.Pdf`](../api/main.html#pikepdf.Pdf). Closing the `Pdf` with
[`pikepdf.Pdf.close()`](../api/main.html#pikepdf.Pdf.close) will invalidate some objects, depending on whether
or not the data was loaded, and other implementation details that may change.
Generally speaking, a [`pikepdf.Pdf`](../api/main.html#pikepdf.Pdf) should be held open until it is no
longer needed, and objects that were derived from it may or may not be usable
after it is closed.

Simple objects (booleans, integers, decimals, `None`) are copied directly
to Python as pure Python objects.

For PDF stream objects, use [`pikepdf.Object.read_bytes()`](../api/main.html#pikepdf.Object.read_bytes) to obtain a
copy of the object as pure bytes data, if this information is required after
closing a PDF.

When objects are copied from one [`pikepdf.Pdf`](../api/main.html#pikepdf.Pdf) to another, the
underlying data is copied immediately into the target. As such it is possible
to merge hundreds of `Pdf` into one, keeping only a single source at a time and the
target file open.

## Indirect objects[](#indirect-objects)

PDF has two ways to represented a PDF dictionary that contains another dictionary:
it can contain the inner dictionary, or provide a reference to another object.
In the PDF file itself, most objects have an object number that is for referencing.

pikepdf hides the details about whether an object is directly or indirectly
referenced, since in many situations it does not matter and manually testing each
object to see if it needs to be dereferenced before accessing it is tedious.
However, you may need to create indirect references. Sometimes, the [PDF 1.7 Reference Manual](../references/resources.html)
specifically requires that a value be an indirect object.

You can use [`pikepdf.Object.is_indirect`](../api/main.html#pikepdf.Object.is_indirect) to check if an object is actually
an indirect reference. If you require an indirect object, use
[`pikepdf.Pdf.make_indirect()`](../api/main.html#pikepdf.Pdf.make_indirect) to attach the dictionary to a `Pdf` and return
an indirect copy of it. Direct objects are not attached to any particular `Pdf`
and can be copied from one to another, just like scalars. Indirect objects
must be attached.

Stream objects are always indirect objects, and must always be attached to a
PDF.

## Object helpers[](#object-helpers)

pikepdf also provides [`pikepdf.ObjectHelper`](../api/models.html#pikepdf.ObjectHelper) and various subclasses of
this class. Usually these are wrappers around a [`pikepdf.Dictionary`](../api/main.html#pikepdf.Dictionary) with
special rules applicable to that type of dictionary. [`pikepdf.Page`](../api/models.html#pikepdf.Page) is
an example of an object helper. The underlying object can be accessed with
[`pikepdf.ObjectHelper.obj`](../api/models.html#pikepdf.ObjectHelper.obj).

---
# Metadata
Source: https://pikepdf.readthedocs.io/en/latest/topics/metadata.html

# Metadata[](#metadata)

PDF has two different types of metadata: XMP metadata, and DocumentInfo, which
is deprecated and removed as of PDF 2.0, but still relevant. For backward
compatibility, both should contain the same content. pikepdf provides a convenient
interface that coordinates edits to both, but is limited to the most common
metadata features.

XMP (Extensible Metadata Platform) Metadata is a metadata specification in XML
format that is used many formats other than PDF. For full information on XMP,
see Adobe’s [XMP Developer Center](https://www.adobe.com/devnet/xmp.html).
The [XMP Specification](https://github.com/adobe/XMP-Toolkit-SDK/blob/main/docs/XMPSpecificationPart1.pdf) also provides useful information.

pikepdf can read compound metadata quantities, but can only modify scalars. For
more complex changes consider using the `python-xmp-toolkit` library and its
libexempi dependency; but note that it is not capable of synchronizing changes
to the older DocumentInfo metadata.

## Automatic metadata updates[](#automatic-metadata-updates)

By default pikepdf will create a XMP metadata block and set `pdf:PDFVersion`
to a value that matches the PDF version declared elsewhere in the PDF, whenever
a PDF is saved. To suppress this behavior, save with
`pdf.save(..., fix_metadata_version=False)`.

Also by default, `Pdf.open_metadata()` will synchronize the XMP metadata
with the older document information dictionary. This behavior can also be
adjusted using keyword arguments.

## Accessing metadata[](#accessing-metadata)

The XMP metadata stream is attached the PDF’s root object, but to simplify
management of this, use [`pikepdf.Pdf.open_metadata()`](../api/main.html#pikepdf.Pdf.open_metadata). The returned
[`pikepdf.models.PdfMetadata`](../api/models.html#pikepdf.models.PdfMetadata) object may be used for reading, or entered
with a `with` block to modify and commit changes. If you use this interface,
pikepdf will synchronize changes to new and old metadata.

A PDF must still be saved after metadata is changed.

```
&gt;&gt;&gt; pdf = pikepdf.open(&#39;../tests/resources/sandwich.pdf&#39;)

&gt;&gt;&gt; meta = pdf.open_metadata()

&gt;&gt;&gt; meta[&#39;xmp:CreatorTool&#39;]
&#39;ocrmypdf 5.3.3 / Tesseract OCR-PDF 3.05.01&#39;

```

If no XMP metadata exists, an empty XMP metadata container will be created.

Open metadata in a `with` block to open it for editing. When the block is
exited, changes are committed (updating XMP and the Document Info dictionary)
and attached to the PDF object. The PDF must still be saved. If an exception
occurs in the block, changes are discarded.

```
&gt;&gt;&gt; with pdf.open_metadata() as meta:
...     meta[&#39;dc:title&#39;] = &quot;Let&#39;s change the title&quot;
...

```

The list of available metadata fields may be found in the [XMP Specification](https://github.com/adobe/XMP-Toolkit-SDK/blob/main/docs/XMPSpecificationPart1.pdf).

## Removing metadata items[](#removing-metadata-items)

After opening metadata, use `del meta['dc:title']` to delete a metadata entry.

To remove all of a PDF’s metadata records, don’t use `pdf.open_metadata`.
Instead, use `del pdf.Root.Metadata` and `del pdf.docinfo`
to remove the XMP and document info metadata, respectively.

## Checking PDF/A conformance[](#checking-pdf-a-conformance)

The metadata interface can also test if a file **claims** to be conformant
to the PDF/A specification.

```
&gt;&gt;&gt; pdf = pikepdf.open(&#39;../tests/resources/veraPDF test suite 6-2-10-t02-pass-a.pdf&#39;)

&gt;&gt;&gt; meta = pdf.open_metadata()

&gt;&gt;&gt; meta.pdfa_status
&#39;1B&#39;

```

Note

Note that this property merely *tests* if the file claims to be conformant to
the PDF/A standard. Use a tool such as [veraPDF](https://verapdf.org/) (official tool), or third party
web services such as [PDFEN](https://www.pdfen.com/pdf-a-validator) or 3-HEIGHTS™ PDF [VALIDATOR](https://www.pdf-online.com/osa/validate.aspx) to verify conformance.

---
# Form
Source: https://pikepdf.readthedocs.io/en/latest/api/form.html

# Form[](#form)

The `pikepdf.form` module provides a high-level API for working with interactive forms, built on top of the lower-level `pikepdf.AcroForm` interface.

Support for working with interactive forms.

*class *pikepdf.form.Form(*pdf*, *generate_appearances=None*, ***, *ignore_max_length=False*)[](#pikepdf.form.Form)
: 
Utility class to make it easier to work with interactive forms.

This is easier to use than the core {class}`pikepdf.AcroForm` implementation, but is
higher-level, and abstracts over details in ways which do impose some limitations,
such as failing for PDFs which have multiple fields with the same name.

A non-exhaustive list of limitations:

- 
No support for signatures

- 
No support for password fields

- 
No support for rich text fields

- 
Multiselect choice fields are treated as single-select

- 
Generating appearance streams imposes additional limitations (see
{class}`pikepdf.form.DefaultAppearanceStreamGenerator` and
{class}`pikepdf.form.ExtendedAppearanceStreamGenerator` for details.)

**Parameters:**

- 
**pdf** ([*pikepdf.Pdf*](main.html#pikepdf.Pdf))

- 
**generate_appearances** (*type**[*[*AppearanceStreamGenerator*](#pikepdf.form.AppearanceStreamGenerator)*] **| **None*)

generate_appearances*: [AppearanceStreamGenerator](#pikepdf.form.AppearanceStreamGenerator) | None** = None*[](#pikepdf.form.Form.generate_appearances)
: 
If provided, this object will be used to generate appearance streams for fields
as the form is filled. If not, the needs_appearances flag will be set on the form.

ignore_max_length*: bool*[](#pikepdf.form.Form.ignore_max_length)
: 
If True, we will ignore the MaxLen property of any text fields in this form. This
produces a PDF that would typically not be possible to create in an interactive PDF
reader, but this may be desirable or useful if the PDF is intended to be read by
another automated system rather than a human.

items()[](#pikepdf.form.Form.items)
: 
Yield (name, field) pairs for all fields in this form.

**Return type:**

collections.abc.Generator[tuple[str, [_FieldWrapper](#pikepdf.form._FieldWrapper)]]

## Form Fields[](#form-fields)

*class *pikepdf.form._FieldWrapper(*form*, *field*)[](#pikepdf.form._FieldWrapper)
: 
Base class for other field types.

In addition to the methods and properties documented here, all fields expose the
same properties and methods defined on pikepdf.AcroFormField. These are forwarded
to the underlying field object.

**Parameters:**

- 
**form** ([*Form*](#pikepdf.form.Form))

- 
**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

*property *export_enabled*: bool*[](#pikepdf.form._FieldWrapper.export_enabled)
: 
Should this field’s value be included when exporting data from the PDF?

**Return type:**

bool

*property *is_read_only*: bool*[](#pikepdf.form._FieldWrapper.is_read_only)
: 
Is this a read-only field?

**Return type:**

bool

*property *is_required*: bool*[](#pikepdf.form._FieldWrapper.is_required)
: 
Is this a required field?

**Return type:**

bool

*class *pikepdf.form.TextField(*form*, *field*)[](#pikepdf.form.TextField)
: 
Represents an editable text field.

**Parameters:**

- 
**form** ([*Form*](#pikepdf.form.Form))

- 
**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

*property *default_value*: str*[](#pikepdf.form.TextField.default_value)
: 
The default (placeholder) value of the text field.

**Return type:**

str

*property *is_combed*: bool*[](#pikepdf.form.TextField.is_combed)
: 
Is this a combed text field?

If True, the field will be split into equal-length segments, based on
`max_length`, containing one character each.

**Return type:**

bool

*property *is_file_select*: bool*[](#pikepdf.form.TextField.is_file_select)
: 
Is this a file select field?

File select fields are not currently implemented, but this flag is presented for
your information.

**Return type:**

bool

*property *is_multiline*: bool*[](#pikepdf.form.TextField.is_multiline)
: 
Is this a multiline text field?

If True, text will be wrapped and newlines will be allowed. If False, text will
not be wrapped and newlines are stripped.

**Return type:**

bool

*property *is_password*: bool*[](#pikepdf.form.TextField.is_password)
: 
Is this a password field?

Password fields are not currently implemented, but this flag is presented for
your information.

**Return type:**

bool

*property *is_rich_text*: bool*[](#pikepdf.form.TextField.is_rich_text)
: 
Is this a rich text field?

Rich text functionality is not currently implemented, but this flag is presented
for your information.

**Return type:**

bool

*property *max_length*: int | None*[](#pikepdf.form.TextField.max_length)
: 
The maximum length of the text in this field.

**Return type:**

int | None

*property *scrolling_enabled*: bool*[](#pikepdf.form.TextField.scrolling_enabled)
: 
Should scrolling (horizontal or vertical) be allowed in this field?

**Return type:**

bool

*property *spell_check_enabled*: bool*[](#pikepdf.form.TextField.spell_check_enabled)
: 
Should spell-checking be enabled in this field?

**Return type:**

bool

*property *value*: str*[](#pikepdf.form.TextField.value)
: 
The value of the text field.

**Return type:**

str

*class *pikepdf.form.CheckboxField(*form*, *field*)[](#pikepdf.form.CheckboxField)
: 
Represents a checkbox field.

**Parameters:**

- 
**form** ([*Form*](#pikepdf.form.Form))

- 
**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

*property *checked*: bool*[](#pikepdf.form.CheckboxField.checked)
: 
Is this checkbox checked?

**Return type:**

bool

*property *on_value*: [pikepdf.Name](main.html#pikepdf.Name)*[](#pikepdf.form.CheckboxField.on_value)
: 
The underlying value associated with this checkbox’s “on” state.

**Return type:**

[pikepdf.Name](main.html#pikepdf.Name)

*property *states*: collections.abc.Sequence[[pikepdf.Name](main.html#pikepdf.Name)]*[](#pikepdf.form.CheckboxField.states)
: 
List the possible states for this checkbox.

Typically this will be /Off plus one additional arbitrary value representing the
on state.

**Return type:**

collections.abc.Sequence[[pikepdf.Name](main.html#pikepdf.Name)]

*property *value*: [pikepdf.Name](main.html#pikepdf.Name) | None*[](#pikepdf.form.CheckboxField.value)
: 
The actual current stored value of this checkbox.

**Return type:**

[pikepdf.Name](main.html#pikepdf.Name) | None

*class *pikepdf.form.RadioButtonGroup(*form*, *field*)[](#pikepdf.form.RadioButtonGroup)
: 
Represents a radio button group.

**Parameters:**

- 
**form** ([*Form*](#pikepdf.form.Form))

- 
**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

*property *can_toggle_off[](#pikepdf.form.RadioButtonGroup.can_toggle_off)
: 
If radio buttons in this group are allowed to be togged off.

*property *options*: collections.abc.Sequence[[RadioButtonOption](#pikepdf.form.RadioButtonOption)]*[](#pikepdf.form.RadioButtonGroup.options)
: 
A list of all available options.

**Return type:**

collections.abc.Sequence[[RadioButtonOption](#pikepdf.form.RadioButtonOption)]

*property *selected*: [RadioButtonOption](#pikepdf.form.RadioButtonOption) | None*[](#pikepdf.form.RadioButtonGroup.selected)
: 
The currently selected option.

**Return type:**

[RadioButtonOption](#pikepdf.form.RadioButtonOption) | None

*property *states*: collections.abc.Sequence[[pikepdf.Name](main.html#pikepdf.Name)]*[](#pikepdf.form.RadioButtonGroup.states)
: 
List the possible on states of all component radio buttons in this group.

**Return type:**

collections.abc.Sequence[[pikepdf.Name](main.html#pikepdf.Name)]

*property *value*: [pikepdf.Name](main.html#pikepdf.Name) | None*[](#pikepdf.form.RadioButtonGroup.value)
: 
The value of the currently selected option.

**Return type:**

[pikepdf.Name](main.html#pikepdf.Name) | None

*class *pikepdf.form.RadioButtonOption(*group*, *annot_dict*, *index*)[](#pikepdf.form.RadioButtonOption)
: 
Represents a single radio button in a radio button group.

**Parameters:**

- 
**group** ([*RadioButtonGroup*](#pikepdf.form.RadioButtonGroup))

- 
**annot_dict** ([*pikepdf.Dictionary*](main.html#pikepdf.Dictionary))

- 
**index** (*int*)

*property *checked*: bool*[](#pikepdf.form.RadioButtonOption.checked)
: 
Is this is the currently selected option?

**Return type:**

bool

*property *on_value*: [pikepdf.Name](main.html#pikepdf.Name)*[](#pikepdf.form.RadioButtonOption.on_value)
: 
The underlying value associated with this button’s “on” state.

**Return type:**

[pikepdf.Name](main.html#pikepdf.Name)

select()[](#pikepdf.form.RadioButtonOption.select)
: 
Mark this as the selected option.

*property *states*: collections.abc.Sequence[[pikepdf.Name](main.html#pikepdf.Name)]*[](#pikepdf.form.RadioButtonOption.states)
: 
List the possible states for this radio button.

Typically this will be /Off plus one additional arbitrary value representing the
on state.

**Return type:**

collections.abc.Sequence[[pikepdf.Name](main.html#pikepdf.Name)]

*class *pikepdf.form.PushbuttonField(*form*, *field*)[](#pikepdf.form.PushbuttonField)
: 
Represents a pushbutton field.

Pushbuttons retain no permanent state, so this class is merely a placeholder. It
exposes no functionality.

**Parameters:**

- 
**form** ([*Form*](#pikepdf.form.Form))

- 
**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

*class *pikepdf.form.ChoiceField(*form*, *field*)[](#pikepdf.form.ChoiceField)
: 
Represents a choice field.

Multiselect is not currently supported; multiselect fields will still only allow
selecting a single value.

**Parameters:**

- 
**form** ([*Form*](#pikepdf.form.Form))

- 
**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

*property *allow_edit*: bool*[](#pikepdf.form.ChoiceField.allow_edit)
: 
Does this field include an editable text box in addition to the dropdown?

The field must be a comboxbox; this option is not valid for list boxes.

**Return type:**

bool

*property *is_combobox*: bool*[](#pikepdf.form.ChoiceField.is_combobox)
: 
Is this a combobox field? If false, this is instead a list box.

**Return type:**

bool

*property *is_multiselect*: bool*[](#pikepdf.form.ChoiceField.is_multiselect)
: 
Is this a multiselect field?

Multiselect fields are currently treated as single-selection fields. True
multiselect is not yet supported, but this flag is presented for your
information.

**Return type:**

bool

*property *options*: collections.abc.Sequence[[ChoiceFieldOption](#pikepdf.form.ChoiceFieldOption)]*[](#pikepdf.form.ChoiceField.options)
: 
A list of all available options.

**Return type:**

collections.abc.Sequence[[ChoiceFieldOption](#pikepdf.form.ChoiceFieldOption)]

*property *selected*: [ChoiceFieldOption](#pikepdf.form.ChoiceFieldOption) | None*[](#pikepdf.form.ChoiceField.selected)
: 
The currently selected option, or None if no option is selected.

**Return type:**

[ChoiceFieldOption](#pikepdf.form.ChoiceFieldOption) | None

*property *spell_check_enabled*: bool*[](#pikepdf.form.ChoiceField.spell_check_enabled)
: 
Should spell-checking be enabled in this field?

This is only valid for fields that allow editing.

**Return type:**

bool

*property *value*: str | None*[](#pikepdf.form.ChoiceField.value)
: 
The value of the currently selected option.

**Return type:**

str | None

*class *pikepdf.form.ChoiceFieldOption(*field*, *opt*, *index*)[](#pikepdf.form.ChoiceFieldOption)
: 
Represents a single option for a choice field.

**Parameters:**

- 
**field** ([*ChoiceField*](#pikepdf.form.ChoiceField))

- 
**opt** ([*pikepdf.String*](main.html#pikepdf.String)* | *[*pikepdf.Array*](main.html#pikepdf.Array))

- 
**index** (*int** | **None*)

*property *display_value[](#pikepdf.form.ChoiceFieldOption.display_value)
: 
The value that will be displayed on-screen to the user in a PDF reader.

*property *export_value[](#pikepdf.form.ChoiceFieldOption.export_value)
: 
The value that will be used when exporting data from this form.

*property *is_hidden*: bool*[](#pikepdf.form.ChoiceFieldOption.is_hidden)
: 
Is this option hidden?

Hidden options are still settable via code, but are not shown to users in PDF
reader applications.

**Return type:**

bool

*property *is_preset*: bool*[](#pikepdf.form.ChoiceFieldOption.is_preset)
: 
Is this option one of the field’s preset options?

If false, this is a manually entered value typed by the user in an editable
choice field.

**Return type:**

bool

select()[](#pikepdf.form.ChoiceFieldOption.select)
: 
Set this option as the selected option.

*property *selected*: bool*[](#pikepdf.form.ChoiceFieldOption.selected)
: 
Is this the currently selected option?

**Return type:**

bool

*class *pikepdf.form.SignatureField(*form*, *field*)[](#pikepdf.form.SignatureField)
: 
Represents a signature field.

Signatures are not truly supported.

**Parameters:**

- 
**form** ([*Form*](#pikepdf.form.Form))

- 
**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

stamp_overlay(*overlay*, ***, *expand_rect=None*)[](#pikepdf.form.SignatureField.stamp_overlay)
: 
Stamp an image over the top of a signature field.

This is *not* true support for PDF signatures. Rather, it is merely a utility
for adding an image to the PDF at the location of a signature field.

This uses pikepdf.Page.add_overlay under the hood, see that method for
additional usage information.

If the bounding box of the signature field is smaller than the “visual”
signature area in the PDF, you may use the `expand_rect` parameter to increase
the dimensions of the rectangle when stamping. This may be any of the
following types:

- 
A number, which will be added equally to all sides of the box

- 
A sequence of two numbers, which will be added on the X and Y axis,
respectively

- 
A sequence of four numbers, which will be added to the left, bottom, right,
and top sides respectively

Positive numbers will increase the size of the box, and negative numbers will
decease it.

**Parameters:**

- 
**overlay** ([*pikepdf.Object*](main.html#pikepdf.Object)* | *[*pikepdf.Page*](models.html#pikepdf.Page))

- 
**expand_rect** (*int** | **float** | **decimal.Decimal** | **collections.abc.Sequence**[**int** | **float** | **decimal.Decimal**] **| **None*)

**Return type:**
: 
[pikepdf.Name](main.html#pikepdf.Name)

## Generating Appearance Streams[](#generating-appearance-streams)

Merely setting the values of form fields is not sufficient. It is also necessary to
generate appearance streams for fields. These appearance streams define how the filled-out
field should actually look when viewed in a PDF reader.

Generating appearance streams can be very complex. Both of the classes below have limited
capacities, but should work for many use cases, and can be extended to meet your needs.

*class *pikepdf.form.AppearanceStreamGenerator(*pdf*, *form*)[](#pikepdf.form.AppearanceStreamGenerator)
: 
Appearance stream generators are used to render forms.

They are used by the pikepdf.form.Form class to optionally generate appearance
streams as forms are filled.

**Parameters:**

- 
**pdf** ([*pikepdf.Pdf*](main.html#pikepdf.Pdf))

- 
**form** ([*pikepdf.AcroForm*](models.html#pikepdf.AcroForm))

form*: [pikepdf.AcroForm](models.html#pikepdf.AcroForm)*[](#pikepdf.form.AppearanceStreamGenerator.form)
: 

*abstractmethod *generate_choice(*field*)[](#pikepdf.form.AppearanceStreamGenerator.generate_choice)
: 
Generate the appearance stream for a choice field.

**Parameters:**

**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

*abstractmethod *generate_text(*field*)[](#pikepdf.form.AppearanceStreamGenerator.generate_text)
: 
Generate the appearance stream for a text field.

**Parameters:**

**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

pdf*: [pikepdf.Pdf](main.html#pikepdf.Pdf)*[](#pikepdf.form.AppearanceStreamGenerator.pdf)
: 

*class *pikepdf.form.DefaultAppearanceStreamGenerator(*pdf*, *form*)[](#pikepdf.form.DefaultAppearanceStreamGenerator)
: 
Basic appearance stream generator using QPDF’s default algorithm.

It is thus subject to all the same
[limitations](https://qpdf.readthedocs.io/en/stable/cli.html#option-generate-appearances).

Briefly summarized, these limitations are:

- 
Cannot generate appearance streams using encodings other than ASCII, WinAnsi, or
MacRoman

- 
No support for multiline text

- 
No support for auto-sized text

- 
Does not respect quadding

Using this class will produce the same results as the following code:

```
form = Form(pdf, generate_appearances = None)
...
pdf.generate_appearances()

```

However, unlike the above, appearances will be generated on the fly as the form is
filled out, rather than all at once at the end.

You may extend this class to customize appearance streams or add support for
features you need.

**Parameters:**

- 
**pdf** ([*pikepdf.Pdf*](main.html#pikepdf.Pdf))

- 
**form** ([*pikepdf.AcroForm*](models.html#pikepdf.AcroForm))

generate_choice(*field*)[](#pikepdf.form.DefaultAppearanceStreamGenerator.generate_choice)
: 
Generate the appearance stream for a choice field.

**Parameters:**

**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

generate_text(*field*)[](#pikepdf.form.DefaultAppearanceStreamGenerator.generate_text)
: 
Generate the appearance stream for a text field.

**Parameters:**

**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

*class *pikepdf.form.ExtendedAppearanceStreamGenerator(*pdf*, *form*)[](#pikepdf.form.ExtendedAppearanceStreamGenerator)
: 
Alternate appearance stream generator to address limitations of the default one.

**Improved features include:**

- 
Supports multiline text fields, with caveats:

- 
Word wrap does not take scaling factors (other than font size) into account

- 
Spacing operators not taken into consideration either

- 
Quadding is still ignored

- 
Due to limitations in Firefox’s PDF viewer, the font and the line breaks will be
incorrect when viewed in Firefox. PDFs filled by full-fat PDF readers, including
Adobe Acrobat Reader, exhibit the same behavior when viewed in Firefox.

- 
Supports combed text fields, with most of the same caveats as above

Otherwise, this implementation has most of the same limitations as the default
implementation. Unlike the default implementation, this is implemented in Python
rather than C++, so will also be less performant.

**Parameters:**
: 

- 
**pdf** ([*pikepdf.Pdf*](main.html#pikepdf.Pdf))

- 
**form** ([*pikepdf.AcroForm*](models.html#pikepdf.AcroForm))

generate_text(*field*)[](#pikepdf.form.ExtendedAppearanceStreamGenerator.generate_text)
: 
Generate the appearance stream for a text field.

**Parameters:**

**field** ([*pikepdf.AcroFormField*](models.html#pikepdf.AcroFormField))

---
# Nametrees
Source: https://pikepdf.readthedocs.io/en/latest/topics/nametrees.html

# Name trees[](#name-trees)

A name trees is a compound data structure in a PDFs, composed from primitive data
types, namely PDF dictionaries and arrays. pikepdf provides an interface that
significantly simplifies this complex data structure, making it as simple as
manipulating any Python dictionary.

In many cases, the [PDF 1.7 Reference Manual](../references/resources.html) specifies that some information is stored in a name
tree. To access and manipulate those objects, use [`pikepdf.NameTree`](../api/models.html#pikepdf.NameTree).

Some objects that are stored in name trees include the objects in
`Pdf.Root.Names`:

- 
`Dests`: named destinations

- 
`URLS`: URLs

- 
`JavaScript`: embedded PDF JavaScript

- 
`Pages`: named pages

- 
`IDS`: digital identifiers

Attached files (or embedded files) are managed in a name tree, but pikepdf
provides an interface specifically for managing them. Use that instead.

```
&gt;&gt;&gt; from pikepdf import Pdf, Page, NameTree

&gt;&gt;&gt; pdf = Pdf.open(&#39;../tests/resources/outlines.pdf&#39;)

&gt;&gt;&gt; nt = NameTree(pdf.Root.Names.Dests)

&gt;&gt;&gt; print([k for k in nt.keys()])
[&#39;0&#39;, &#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, &#39;5&#39;, &#39;6&#39;, &#39;7&#39;, &#39;8&#39;]

&gt;&gt;&gt; nt[&#39;2&#39;][0].objgen, nt[&#39;2&#39;][1], nt[&#39;2&#39;][2]
((3, 0), pikepdf.Name(&quot;/XYZ&quot;), Decimal(&#39;89.29&#39;))

```

---
# Interactive Forms
Source: https://pikepdf.readthedocs.io/en/latest/topics/interactive_forms.html

# Working with interactive forms[](#working-with-interactive-forms)

pikepdf provides two interfaces for working with interactive forms. There is a low-level
interface, [`pikepdf.AcroForm`](../api/models.html#pikepdf.AcroForm), which is exposed as the
[`pikepdf.Pdf.acroform`](../api/main.html#pikepdf.Pdf.acroform) property. There is also a higher-level interface available
in the [`pikepdf.form`](../api/form.html#module-pikepdf.form) module, which provides several abstractions to make usage
easier.

## Extracting Form Data[](#extracting-form-data)

It is relatively easy to extract basic form data from a PDF.

```
&gt;&gt;&gt; from pikepdf.form import Form

&gt;&gt;&gt; form = Form(pdf)

&gt;&gt;&gt; data = {}

&gt;&gt;&gt; for field_name, field in form.items():
...    if field.is_text or field.is_choice or field.is_radio_button:
...        data[field_name] = field.value
...    elif field.is_checkbox:
...        data[field_name] = field.checked

```