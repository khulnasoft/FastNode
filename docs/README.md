<!-- markdownlint-disable -->

# API Overview

## Modules

- [`fastnode.api`](./fastnode.api.md#module-fastnodeapi)
- [`fastnode.api.readyapi_app`](./fastnode.api.readyapi_app.md#module-fastnodeapireadyapi_app)
- [`fastnode.api.readyapi_utils`](./fastnode.api.readyapi_utils.md#module-fastnodeapireadyapi_utils): Collection of utilities for ReadyAPI apps.
- [`fastnode.components`](./fastnode.components.md#module-fastnodecomponents)
- [`fastnode.components.outputs`](./fastnode.components.outputs.md#module-fastnodecomponentsoutputs)
- [`fastnode.components.types`](./fastnode.components.types.md#module-fastnodecomponentstypes)
- [`fastnode.core`](./fastnode.core.md#module-fastnodecore)
- [`fastnode.export`](./fastnode.export.md#module-fastnodeexport)
- [`fastnode.tasks`](./fastnode.tasks.md#module-fastnodetasks)
- [`fastnode.ui`](./fastnode.ui.md#module-fastnodeui)
- [`fastnode.ui.schema_utils`](./fastnode.ui.schema_utils.md#module-fastnodeuischema_utils)
- [`fastnode.ui.streamlit_ui`](./fastnode.ui.streamlit_ui.md#module-fastnodeuistreamlit_ui)
- [`fastnode.ui.streamlit_utils`](./fastnode.ui.streamlit_utils.md#module-fastnodeuistreamlit_utils): Hack to add per-session state to Streamlit.
- [`fastnode.utils`](./fastnode.utils.md#module-fastnodeutils)

## Classes

- [`outputs.ClassificationOutput`](./fastnode.components.outputs.md#class-classificationoutput)
- [`outputs.ScoredLabel`](./fastnode.components.outputs.md#class-scoredlabel)
- [`types.FileContent`](./fastnode.components.types.md#class-filecontent)
- [`core.Fastnode`](./fastnode.core.md#class-fastnode)
- [`export.ExportFormat`](./fastnode.export.md#class-exportformat): An enumeration.
- [`streamlit_ui.InputUI`](./fastnode.ui.streamlit_ui.md#class-inputui)
- [`streamlit_ui.OutputUI`](./fastnode.ui.streamlit_ui.md#class-outputui)
- [`streamlit_utils.SessionState`](./fastnode.ui.streamlit_utils.md#class-sessionstate)

## Functions

- [`readyapi_app.create_api`](./fastnode.api.readyapi_app.md#function-create_api)
- [`readyapi_app.launch_api`](./fastnode.api.readyapi_app.md#function-launch_api)
- [`readyapi_utils.as_form`](./fastnode.api.readyapi_utils.md#function-as_form): Adds an as_form class method to decorated models.
- [`readyapi_utils.patch_readyapi`](./fastnode.api.readyapi_utils.md#function-patch_readyapi): Patch function to allow relative url resolution.
- [`core.get_callable`](./fastnode.core.md#function-get_callable): Import a callable from an string.
- [`core.get_input_type`](./fastnode.core.md#function-get_input_type): Returns the input type of a given function (callable).
- [`core.get_output_type`](./fastnode.core.md#function-get_output_type): Returns the output type of a given function (callable).
- [`core.is_compatible_type`](./fastnode.core.md#function-is_compatible_type): Returns `True` if the type is fastnode-compatible.
- [`core.name_to_title`](./fastnode.core.md#function-name_to_title): Converts a camelCase or snake_case name to title case.
- [`schema_utils.get_single_reference_item`](./fastnode.ui.schema_utils.md#function-get_single_reference_item)
- [`schema_utils.is_multi_enum_property`](./fastnode.ui.schema_utils.md#function-is_multi_enum_property)
- [`schema_utils.is_multi_file_property`](./fastnode.ui.schema_utils.md#function-is_multi_file_property)
- [`schema_utils.is_object_list_property`](./fastnode.ui.schema_utils.md#function-is_object_list_property)
- [`schema_utils.is_property_list`](./fastnode.ui.schema_utils.md#function-is_property_list)
- [`schema_utils.is_single_boolean_property`](./fastnode.ui.schema_utils.md#function-is_single_boolean_property)
- [`schema_utils.is_single_datetime_property`](./fastnode.ui.schema_utils.md#function-is_single_datetime_property)
- [`schema_utils.is_single_dict_property`](./fastnode.ui.schema_utils.md#function-is_single_dict_property)
- [`schema_utils.is_single_enum_property`](./fastnode.ui.schema_utils.md#function-is_single_enum_property)
- [`schema_utils.is_single_file_property`](./fastnode.ui.schema_utils.md#function-is_single_file_property)
- [`schema_utils.is_single_number_property`](./fastnode.ui.schema_utils.md#function-is_single_number_property)
- [`schema_utils.is_single_object`](./fastnode.ui.schema_utils.md#function-is_single_object)
- [`schema_utils.is_single_reference`](./fastnode.ui.schema_utils.md#function-is_single_reference)
- [`schema_utils.is_single_string_property`](./fastnode.ui.schema_utils.md#function-is_single_string_property)
- [`schema_utils.resolve_reference`](./fastnode.ui.schema_utils.md#function-resolve_reference)
- [`streamlit_ui.function_has_named_arg`](./fastnode.ui.streamlit_ui.md#function-function_has_named_arg)
- [`streamlit_ui.has_input_ui_renderer`](./fastnode.ui.streamlit_ui.md#function-has_input_ui_renderer)
- [`streamlit_ui.has_output_ui_renderer`](./fastnode.ui.streamlit_ui.md#function-has_output_ui_renderer)
- [`streamlit_ui.is_compatible_audio`](./fastnode.ui.streamlit_ui.md#function-is_compatible_audio)
- [`streamlit_ui.is_compatible_image`](./fastnode.ui.streamlit_ui.md#function-is_compatible_image)
- [`streamlit_ui.is_compatible_video`](./fastnode.ui.streamlit_ui.md#function-is_compatible_video)
- [`streamlit_ui.launch_ui`](./fastnode.ui.streamlit_ui.md#function-launch_ui)
- [`streamlit_ui.render_streamlit_ui`](./fastnode.ui.streamlit_ui.md#function-render_streamlit_ui)
- [`streamlit_utils.get_current_session`](./fastnode.ui.streamlit_utils.md#function-get_current_session)
- [`streamlit_utils.get_session_state`](./fastnode.ui.streamlit_utils.md#function-get_session_state): Gets a SessionState object for the current session.


---

_This file was automatically generated via [docsai](https://github.com/khulnasoft/docsai)._
