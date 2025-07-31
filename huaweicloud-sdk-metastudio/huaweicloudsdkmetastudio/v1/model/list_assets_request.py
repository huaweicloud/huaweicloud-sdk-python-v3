# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'name': 'str',
        'tag': 'str',
        'tag_combination_type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'asset_type': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'asset_source': 'str',
        'asset_state': 'str',
        'style_id': 'str',
        'accurate_query_field': 'list[str]',
        'asset_id': 'list[str]',
        'sex': 'str',
        'language': 'str',
        'system_property': 'str',
        'action_editable': 'bool',
        'is_with_action_library': 'bool',
        'is_movable': 'bool',
        'voice_provider': 'str',
        'role': 'str',
        'is_realtime_voice': 'bool',
        'human_model_2d_version': 'str',
        'include_device_name': 'str',
        'exclude_device_name': 'str',
        'supported_service': 'str',
        'app_user_id': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'tag': 'tag',
        'tag_combination_type': 'tag_combination_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'asset_type': 'asset_type',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'asset_source': 'asset_source',
        'asset_state': 'asset_state',
        'style_id': 'style_id',
        'accurate_query_field': 'accurate_query_field',
        'asset_id': 'asset_id',
        'sex': 'sex',
        'language': 'language',
        'system_property': 'system_property',
        'action_editable': 'action_editable',
        'is_with_action_library': 'is_with_action_library',
        'is_movable': 'is_movable',
        'voice_provider': 'voice_provider',
        'role': 'role',
        'is_realtime_voice': 'is_realtime_voice',
        'human_model_2d_version': 'human_model_2d_version',
        'include_device_name': 'include_device_name',
        'exclude_device_name': 'exclude_device_name',
        'supported_service': 'supported_service',
        'app_user_id': 'app_user_id'
    }

    def __init__(self, x_app_user_id=None, limit=None, offset=None, name=None, tag=None, tag_combination_type=None, start_time=None, end_time=None, asset_type=None, sort_key=None, sort_dir=None, asset_source=None, asset_state=None, style_id=None, accurate_query_field=None, asset_id=None, sex=None, language=None, system_property=None, action_editable=None, is_with_action_library=None, is_movable=None, voice_provider=None, role=None, is_realtime_voice=None, human_model_2d_version=None, include_device_name=None, exclude_device_name=None, supported_service=None, app_user_id=None):
        r"""ListAssetsRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param name: 按名称模糊查询。
        :type name: str
        :param tag: 按标签模糊查询。
        :type tag: str
        :param tag_combination_type: 标签查询组合方式 INTERSECTION：交集 UNION_SET：并集
        :type tag_combination_type: str
        :param start_time: 起始时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type start_time: str
        :param end_time: 结束时间。格式遵循：RFC 3339 如\&quot;2021-01-10T10:43:17Z\&quot;。
        :type end_time: str
        :param asset_type: 资产类型。多个类型使用英文逗号分隔。 * VOICE_MODEL：音色模型（仅系统管理员可上传） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * HUMAN_MODEL_2D: 2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐 * AUDIO: 音频
        :type asset_type: str
        :param sort_key: 排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order
        :type sort_key: str
        :param sort_dir: 排序方式。 * asc：升序 * desc：降序  默认asc升序。
        :type sort_dir: str
        :param asset_source: 资产来源。 * SYSTEM：系统资产 * CUSTOMIZATION：租户资产 * ALL：所有资产  默认查询租户资产。
        :type asset_source: str
        :param asset_state: 资产状态。多个资产状态使用英文逗号分隔。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK：资产被冻结，资产不可用，不可查看文件。 * WAITING_DELETE：资产将被下线 默认查询所有状态的资产。
        :type asset_state: str
        :param style_id: 基于风格化ID查询关联资产。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02  * system_female_002：女性风格02
        :type style_id: str
        :param accurate_query_field: 使用精确查询的字段
        :type accurate_query_field: list[str]
        :param asset_id: 资产id
        :type asset_id: list[str]
        :param sex: 性别。多选使用英文逗号分隔。
        :type sex: str
        :param language: 语言。多选使用英文逗号分隔。
        :type language: str
        :param system_property: 系统属性。  key和value间用\&quot;:\&quot;分隔，多个key之间用\&quot;,\&quot;分隔。  如system_property&#x3D;BACKGROUND_IMG:Yes,RENDER_ENGINE:MetaEngine。  不同Key对应Value取值如下：  公共资产属性： * BACKGROUND_IMG：视频制作的2D背景图片，可取值Yes * CREATED_BY_PLATFORM：是否平台生成，可取值Yes  分身数字人资产属性： * MATERIAL_IMG：素材图片，用作前景。可取值Yes * MATERIAL_VIDEO：素材视频，用作前景。可取值Yes  数字人资产属性： * BACKGROUND_SCENE：视频制作的2D背景场景，可取值Horizontal（横屏）或者Vertical（竖屏）
        :type system_property: str
        :param action_editable: 动作是否可编辑。仅在分身数字人模型查询时有效。
        :type action_editable: bool
        :param is_with_action_library: 分身数字人是否带原子动作库。 &gt; * 带原子动作库的分身数字人可做动作编排。
        :type is_with_action_library: bool
        :param is_movable: 分身数字人是否支持走动。仅在分身数字人模型查询时有效。
        :type is_movable: bool
        :param voice_provider: 取值：HUAWEI_METASTUDIO、MOBVOI。 HUAWEI_METASTUDIO：MetaStudio自研音色 MOBVOI：出门问问音色
        :type voice_provider: str
        :param role: 角色。 SHARER：共享方，SHAREE：被共享方
        :type role: str
        :param is_realtime_voice: 音色是否支持实时合成。仅在音色查询时有效。 &gt; * 支持实时合成的音色，可以用于直播和智能交互场景。否则只能用于视频制作。
        :type is_realtime_voice: bool
        :param human_model_2d_version: 模型版本
        :type human_model_2d_version: str
        :param include_device_name: 资产已执行的任务名称
        :type include_device_name: str
        :param exclude_device_name: 资产已执行的任务名称
        :type exclude_device_name: str
        :param supported_service: 资产支持的业务类型。默认查询所有资产。 * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互
        :type supported_service: str
        :param app_user_id: 第三方用户ID。不允许输入中文。
        :type app_user_id: str
        """
        
        

        self._x_app_user_id = None
        self._limit = None
        self._offset = None
        self._name = None
        self._tag = None
        self._tag_combination_type = None
        self._start_time = None
        self._end_time = None
        self._asset_type = None
        self._sort_key = None
        self._sort_dir = None
        self._asset_source = None
        self._asset_state = None
        self._style_id = None
        self._accurate_query_field = None
        self._asset_id = None
        self._sex = None
        self._language = None
        self._system_property = None
        self._action_editable = None
        self._is_with_action_library = None
        self._is_movable = None
        self._voice_provider = None
        self._role = None
        self._is_realtime_voice = None
        self._human_model_2d_version = None
        self._include_device_name = None
        self._exclude_device_name = None
        self._supported_service = None
        self._app_user_id = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if tag is not None:
            self.tag = tag
        if tag_combination_type is not None:
            self.tag_combination_type = tag_combination_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if asset_type is not None:
            self.asset_type = asset_type
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if asset_source is not None:
            self.asset_source = asset_source
        if asset_state is not None:
            self.asset_state = asset_state
        if style_id is not None:
            self.style_id = style_id
        if accurate_query_field is not None:
            self.accurate_query_field = accurate_query_field
        if asset_id is not None:
            self.asset_id = asset_id
        if sex is not None:
            self.sex = sex
        if language is not None:
            self.language = language
        if system_property is not None:
            self.system_property = system_property
        if action_editable is not None:
            self.action_editable = action_editable
        if is_with_action_library is not None:
            self.is_with_action_library = is_with_action_library
        if is_movable is not None:
            self.is_movable = is_movable
        if voice_provider is not None:
            self.voice_provider = voice_provider
        if role is not None:
            self.role = role
        if is_realtime_voice is not None:
            self.is_realtime_voice = is_realtime_voice
        if human_model_2d_version is not None:
            self.human_model_2d_version = human_model_2d_version
        if include_device_name is not None:
            self.include_device_name = include_device_name
        if exclude_device_name is not None:
            self.exclude_device_name = exclude_device_name
        if supported_service is not None:
            self.supported_service = supported_service
        if app_user_id is not None:
            self.app_user_id = app_user_id

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListAssetsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListAssetsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListAssetsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListAssetsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAssetsRequest.

        每页显示的条目数量。

        :return: The limit of this ListAssetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAssetsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListAssetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAssetsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListAssetsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAssetsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListAssetsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListAssetsRequest.

        按名称模糊查询。

        :return: The name of this ListAssetsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAssetsRequest.

        按名称模糊查询。

        :param name: The name of this ListAssetsRequest.
        :type name: str
        """
        self._name = name

    @property
    def tag(self):
        r"""Gets the tag of this ListAssetsRequest.

        按标签模糊查询。

        :return: The tag of this ListAssetsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListAssetsRequest.

        按标签模糊查询。

        :param tag: The tag of this ListAssetsRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def tag_combination_type(self):
        r"""Gets the tag_combination_type of this ListAssetsRequest.

        标签查询组合方式 INTERSECTION：交集 UNION_SET：并集

        :return: The tag_combination_type of this ListAssetsRequest.
        :rtype: str
        """
        return self._tag_combination_type

    @tag_combination_type.setter
    def tag_combination_type(self, tag_combination_type):
        r"""Sets the tag_combination_type of this ListAssetsRequest.

        标签查询组合方式 INTERSECTION：交集 UNION_SET：并集

        :param tag_combination_type: The tag_combination_type of this ListAssetsRequest.
        :type tag_combination_type: str
        """
        self._tag_combination_type = tag_combination_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ListAssetsRequest.

        起始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The start_time of this ListAssetsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListAssetsRequest.

        起始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param start_time: The start_time of this ListAssetsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAssetsRequest.

        结束时间。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"。

        :return: The end_time of this ListAssetsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAssetsRequest.

        结束时间。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"。

        :param end_time: The end_time of this ListAssetsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ListAssetsRequest.

        资产类型。多个类型使用英文逗号分隔。 * VOICE_MODEL：音色模型（仅系统管理员可上传） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * HUMAN_MODEL_2D: 2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐 * AUDIO: 音频

        :return: The asset_type of this ListAssetsRequest.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ListAssetsRequest.

        资产类型。多个类型使用英文逗号分隔。 * VOICE_MODEL：音色模型（仅系统管理员可上传） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * HUMAN_MODEL_2D: 2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐 * AUDIO: 音频

        :param asset_type: The asset_type of this ListAssetsRequest.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListAssetsRequest.

        排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order

        :return: The sort_key of this ListAssetsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListAssetsRequest.

        排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order

        :param sort_key: The sort_key of this ListAssetsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListAssetsRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :return: The sort_dir of this ListAssetsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListAssetsRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :param sort_dir: The sort_dir of this ListAssetsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def asset_source(self):
        r"""Gets the asset_source of this ListAssetsRequest.

        资产来源。 * SYSTEM：系统资产 * CUSTOMIZATION：租户资产 * ALL：所有资产  默认查询租户资产。

        :return: The asset_source of this ListAssetsRequest.
        :rtype: str
        """
        return self._asset_source

    @asset_source.setter
    def asset_source(self, asset_source):
        r"""Sets the asset_source of this ListAssetsRequest.

        资产来源。 * SYSTEM：系统资产 * CUSTOMIZATION：租户资产 * ALL：所有资产  默认查询租户资产。

        :param asset_source: The asset_source of this ListAssetsRequest.
        :type asset_source: str
        """
        self._asset_source = asset_source

    @property
    def asset_state(self):
        r"""Gets the asset_state of this ListAssetsRequest.

        资产状态。多个资产状态使用英文逗号分隔。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK：资产被冻结，资产不可用，不可查看文件。 * WAITING_DELETE：资产将被下线 默认查询所有状态的资产。

        :return: The asset_state of this ListAssetsRequest.
        :rtype: str
        """
        return self._asset_state

    @asset_state.setter
    def asset_state(self, asset_state):
        r"""Sets the asset_state of this ListAssetsRequest.

        资产状态。多个资产状态使用英文逗号分隔。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK：资产被冻结，资产不可用，不可查看文件。 * WAITING_DELETE：资产将被下线 默认查询所有状态的资产。

        :param asset_state: The asset_state of this ListAssetsRequest.
        :type asset_state: str
        """
        self._asset_state = asset_state

    @property
    def style_id(self):
        r"""Gets the style_id of this ListAssetsRequest.

        基于风格化ID查询关联资产。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02  * system_female_002：女性风格02

        :return: The style_id of this ListAssetsRequest.
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        r"""Sets the style_id of this ListAssetsRequest.

        基于风格化ID查询关联资产。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02  * system_female_002：女性风格02

        :param style_id: The style_id of this ListAssetsRequest.
        :type style_id: str
        """
        self._style_id = style_id

    @property
    def accurate_query_field(self):
        r"""Gets the accurate_query_field of this ListAssetsRequest.

        使用精确查询的字段

        :return: The accurate_query_field of this ListAssetsRequest.
        :rtype: list[str]
        """
        return self._accurate_query_field

    @accurate_query_field.setter
    def accurate_query_field(self, accurate_query_field):
        r"""Sets the accurate_query_field of this ListAssetsRequest.

        使用精确查询的字段

        :param accurate_query_field: The accurate_query_field of this ListAssetsRequest.
        :type accurate_query_field: list[str]
        """
        self._accurate_query_field = accurate_query_field

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ListAssetsRequest.

        资产id

        :return: The asset_id of this ListAssetsRequest.
        :rtype: list[str]
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ListAssetsRequest.

        资产id

        :param asset_id: The asset_id of this ListAssetsRequest.
        :type asset_id: list[str]
        """
        self._asset_id = asset_id

    @property
    def sex(self):
        r"""Gets the sex of this ListAssetsRequest.

        性别。多选使用英文逗号分隔。

        :return: The sex of this ListAssetsRequest.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this ListAssetsRequest.

        性别。多选使用英文逗号分隔。

        :param sex: The sex of this ListAssetsRequest.
        :type sex: str
        """
        self._sex = sex

    @property
    def language(self):
        r"""Gets the language of this ListAssetsRequest.

        语言。多选使用英文逗号分隔。

        :return: The language of this ListAssetsRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ListAssetsRequest.

        语言。多选使用英文逗号分隔。

        :param language: The language of this ListAssetsRequest.
        :type language: str
        """
        self._language = language

    @property
    def system_property(self):
        r"""Gets the system_property of this ListAssetsRequest.

        系统属性。  key和value间用\":\"分隔，多个key之间用\",\"分隔。  如system_property=BACKGROUND_IMG:Yes,RENDER_ENGINE:MetaEngine。  不同Key对应Value取值如下：  公共资产属性： * BACKGROUND_IMG：视频制作的2D背景图片，可取值Yes * CREATED_BY_PLATFORM：是否平台生成，可取值Yes  分身数字人资产属性： * MATERIAL_IMG：素材图片，用作前景。可取值Yes * MATERIAL_VIDEO：素材视频，用作前景。可取值Yes  数字人资产属性： * BACKGROUND_SCENE：视频制作的2D背景场景，可取值Horizontal（横屏）或者Vertical（竖屏）

        :return: The system_property of this ListAssetsRequest.
        :rtype: str
        """
        return self._system_property

    @system_property.setter
    def system_property(self, system_property):
        r"""Sets the system_property of this ListAssetsRequest.

        系统属性。  key和value间用\":\"分隔，多个key之间用\",\"分隔。  如system_property=BACKGROUND_IMG:Yes,RENDER_ENGINE:MetaEngine。  不同Key对应Value取值如下：  公共资产属性： * BACKGROUND_IMG：视频制作的2D背景图片，可取值Yes * CREATED_BY_PLATFORM：是否平台生成，可取值Yes  分身数字人资产属性： * MATERIAL_IMG：素材图片，用作前景。可取值Yes * MATERIAL_VIDEO：素材视频，用作前景。可取值Yes  数字人资产属性： * BACKGROUND_SCENE：视频制作的2D背景场景，可取值Horizontal（横屏）或者Vertical（竖屏）

        :param system_property: The system_property of this ListAssetsRequest.
        :type system_property: str
        """
        self._system_property = system_property

    @property
    def action_editable(self):
        r"""Gets the action_editable of this ListAssetsRequest.

        动作是否可编辑。仅在分身数字人模型查询时有效。

        :return: The action_editable of this ListAssetsRequest.
        :rtype: bool
        """
        return self._action_editable

    @action_editable.setter
    def action_editable(self, action_editable):
        r"""Sets the action_editable of this ListAssetsRequest.

        动作是否可编辑。仅在分身数字人模型查询时有效。

        :param action_editable: The action_editable of this ListAssetsRequest.
        :type action_editable: bool
        """
        self._action_editable = action_editable

    @property
    def is_with_action_library(self):
        r"""Gets the is_with_action_library of this ListAssetsRequest.

        分身数字人是否带原子动作库。 > * 带原子动作库的分身数字人可做动作编排。

        :return: The is_with_action_library of this ListAssetsRequest.
        :rtype: bool
        """
        return self._is_with_action_library

    @is_with_action_library.setter
    def is_with_action_library(self, is_with_action_library):
        r"""Sets the is_with_action_library of this ListAssetsRequest.

        分身数字人是否带原子动作库。 > * 带原子动作库的分身数字人可做动作编排。

        :param is_with_action_library: The is_with_action_library of this ListAssetsRequest.
        :type is_with_action_library: bool
        """
        self._is_with_action_library = is_with_action_library

    @property
    def is_movable(self):
        r"""Gets the is_movable of this ListAssetsRequest.

        分身数字人是否支持走动。仅在分身数字人模型查询时有效。

        :return: The is_movable of this ListAssetsRequest.
        :rtype: bool
        """
        return self._is_movable

    @is_movable.setter
    def is_movable(self, is_movable):
        r"""Sets the is_movable of this ListAssetsRequest.

        分身数字人是否支持走动。仅在分身数字人模型查询时有效。

        :param is_movable: The is_movable of this ListAssetsRequest.
        :type is_movable: bool
        """
        self._is_movable = is_movable

    @property
    def voice_provider(self):
        r"""Gets the voice_provider of this ListAssetsRequest.

        取值：HUAWEI_METASTUDIO、MOBVOI。 HUAWEI_METASTUDIO：MetaStudio自研音色 MOBVOI：出门问问音色

        :return: The voice_provider of this ListAssetsRequest.
        :rtype: str
        """
        return self._voice_provider

    @voice_provider.setter
    def voice_provider(self, voice_provider):
        r"""Sets the voice_provider of this ListAssetsRequest.

        取值：HUAWEI_METASTUDIO、MOBVOI。 HUAWEI_METASTUDIO：MetaStudio自研音色 MOBVOI：出门问问音色

        :param voice_provider: The voice_provider of this ListAssetsRequest.
        :type voice_provider: str
        """
        self._voice_provider = voice_provider

    @property
    def role(self):
        r"""Gets the role of this ListAssetsRequest.

        角色。 SHARER：共享方，SHAREE：被共享方

        :return: The role of this ListAssetsRequest.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this ListAssetsRequest.

        角色。 SHARER：共享方，SHAREE：被共享方

        :param role: The role of this ListAssetsRequest.
        :type role: str
        """
        self._role = role

    @property
    def is_realtime_voice(self):
        r"""Gets the is_realtime_voice of this ListAssetsRequest.

        音色是否支持实时合成。仅在音色查询时有效。 > * 支持实时合成的音色，可以用于直播和智能交互场景。否则只能用于视频制作。

        :return: The is_realtime_voice of this ListAssetsRequest.
        :rtype: bool
        """
        return self._is_realtime_voice

    @is_realtime_voice.setter
    def is_realtime_voice(self, is_realtime_voice):
        r"""Sets the is_realtime_voice of this ListAssetsRequest.

        音色是否支持实时合成。仅在音色查询时有效。 > * 支持实时合成的音色，可以用于直播和智能交互场景。否则只能用于视频制作。

        :param is_realtime_voice: The is_realtime_voice of this ListAssetsRequest.
        :type is_realtime_voice: bool
        """
        self._is_realtime_voice = is_realtime_voice

    @property
    def human_model_2d_version(self):
        r"""Gets the human_model_2d_version of this ListAssetsRequest.

        模型版本

        :return: The human_model_2d_version of this ListAssetsRequest.
        :rtype: str
        """
        return self._human_model_2d_version

    @human_model_2d_version.setter
    def human_model_2d_version(self, human_model_2d_version):
        r"""Sets the human_model_2d_version of this ListAssetsRequest.

        模型版本

        :param human_model_2d_version: The human_model_2d_version of this ListAssetsRequest.
        :type human_model_2d_version: str
        """
        self._human_model_2d_version = human_model_2d_version

    @property
    def include_device_name(self):
        r"""Gets the include_device_name of this ListAssetsRequest.

        资产已执行的任务名称

        :return: The include_device_name of this ListAssetsRequest.
        :rtype: str
        """
        return self._include_device_name

    @include_device_name.setter
    def include_device_name(self, include_device_name):
        r"""Sets the include_device_name of this ListAssetsRequest.

        资产已执行的任务名称

        :param include_device_name: The include_device_name of this ListAssetsRequest.
        :type include_device_name: str
        """
        self._include_device_name = include_device_name

    @property
    def exclude_device_name(self):
        r"""Gets the exclude_device_name of this ListAssetsRequest.

        资产已执行的任务名称

        :return: The exclude_device_name of this ListAssetsRequest.
        :rtype: str
        """
        return self._exclude_device_name

    @exclude_device_name.setter
    def exclude_device_name(self, exclude_device_name):
        r"""Sets the exclude_device_name of this ListAssetsRequest.

        资产已执行的任务名称

        :param exclude_device_name: The exclude_device_name of this ListAssetsRequest.
        :type exclude_device_name: str
        """
        self._exclude_device_name = exclude_device_name

    @property
    def supported_service(self):
        r"""Gets the supported_service of this ListAssetsRequest.

        资产支持的业务类型。默认查询所有资产。 * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互

        :return: The supported_service of this ListAssetsRequest.
        :rtype: str
        """
        return self._supported_service

    @supported_service.setter
    def supported_service(self, supported_service):
        r"""Sets the supported_service of this ListAssetsRequest.

        资产支持的业务类型。默认查询所有资产。 * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互

        :param supported_service: The supported_service of this ListAssetsRequest.
        :type supported_service: str
        """
        self._supported_service = supported_service

    @property
    def app_user_id(self):
        r"""Gets the app_user_id of this ListAssetsRequest.

        第三方用户ID。不允许输入中文。

        :return: The app_user_id of this ListAssetsRequest.
        :rtype: str
        """
        return self._app_user_id

    @app_user_id.setter
    def app_user_id(self, app_user_id):
        r"""Sets the app_user_id of this ListAssetsRequest.

        第三方用户ID。不允许输入中文。

        :param app_user_id: The app_user_id of this ListAssetsRequest.
        :type app_user_id: str
        """
        self._app_user_id = app_user_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAssetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
