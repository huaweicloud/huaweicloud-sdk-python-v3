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
        'start_time': 'str',
        'end_time': 'str',
        'asset_type': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'asset_source': 'str',
        'asset_state': 'str',
        'style_id': 'str',
        'render_engine': 'str',
        'sex': 'str',
        'language': 'str',
        'system_property': 'str',
        'action_editable': 'bool'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'tag': 'tag',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'asset_type': 'asset_type',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'asset_source': 'asset_source',
        'asset_state': 'asset_state',
        'style_id': 'style_id',
        'render_engine': 'render_engine',
        'sex': 'sex',
        'language': 'language',
        'system_property': 'system_property',
        'action_editable': 'action_editable'
    }

    def __init__(self, x_app_user_id=None, limit=None, offset=None, name=None, tag=None, start_time=None, end_time=None, asset_type=None, sort_key=None, sort_dir=None, asset_source=None, asset_state=None, style_id=None, render_engine=None, sex=None, language=None, system_property=None, action_editable=None):
        """ListAssetsRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 开发者应用作为资产权属的可选字段。
        :type x_app_user_id: str
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param name: 按名称模糊查询。
        :type name: str
        :param tag: 按标签模糊查询。
        :type tag: str
        :param start_time: 起始时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type start_time: str
        :param end_time: 结束时间。格式遵循：RFC 3339 如\&quot;2021-01-10T10:43:17Z\&quot;。
        :type end_time: str
        :param asset_type: 资产类型。多个类型使用英文逗号分割。 * HUMAN_MODEL：数字人模型 * VOICE_MODEL：音色模型（仅系统管理员可上传） * SCENE：场景模型 * ANIMATION：动作动画 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * HUMAN_MODEL_2D: 2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐
        :type asset_type: str
        :param sort_key: 排序字段，目前只支持create_time。
        :type sort_key: str
        :param sort_dir: 排序方式。 * asc：升序 * desc：降序  默认asc升序。
        :type sort_dir: str
        :param asset_source: 资产来源。 * SYSTEM：系统资产 * CUSTOMIZATION：租户资产 * ALL：所有资产  默认查询租户资产。
        :type asset_source: str
        :param asset_state: 资产状态。多个资产状态使用英文逗号分割。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK：资产被冻结，资产不可用，不可查看文件。 默认查询所有状态的资产。
        :type asset_state: str
        :param style_id: 基于风格化ID查询关联资产。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02  * system_female_002：女性风格02
        :type style_id: str
        :param render_engine: 可用引擎。 * UE：UE引擎 * MetaEngine：MetaEngine引擎 &gt; 该字段当前只对MetaEngine白名单用户生效
        :type render_engine: str
        :param sex: 性别。多选使用英文逗号分隔。
        :type sex: str
        :param language: 语言。多选使用英文逗号分隔。
        :type language: str
        :param system_property: 系统属性。  key和value间用\&quot;:\&quot;分隔，多个key之间用\&quot;,\&quot;分隔。  如system_property&#x3D;BACKGROUND_IMG:Yes,RENDER_ENGINE:MetaEngine。  不同Key对应Value取值如下： * STYLE_ID：风格Id * RENDER_ENGINE：引擎类型，可取值UE或MetaEngine * BACKGROUND_IMG：视频制作的2D背景图片，可取值Yes * BACKGROUND_SCENE：视频制作的2D背景场景，可取值Horizontal（横屏）或者Vertical（竖屏） * CREATED_BY_PLATFORM：是否平台生成，可取值Yes
        :type system_property: str
        :param action_editable: 动作是否可编辑。仅在分身数字人模型查询时有效。
        :type action_editable: bool
        """
        
        

        self._x_app_user_id = None
        self._limit = None
        self._offset = None
        self._name = None
        self._tag = None
        self._start_time = None
        self._end_time = None
        self._asset_type = None
        self._sort_key = None
        self._sort_dir = None
        self._asset_source = None
        self._asset_state = None
        self._style_id = None
        self._render_engine = None
        self._sex = None
        self._language = None
        self._system_property = None
        self._action_editable = None
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
        if render_engine is not None:
            self.render_engine = render_engine
        if sex is not None:
            self.sex = sex
        if language is not None:
            self.language = language
        if system_property is not None:
            self.system_property = system_property
        if action_editable is not None:
            self.action_editable = action_editable

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this ListAssetsRequest.

        开发者应用作为资产权属的可选字段。

        :return: The x_app_user_id of this ListAssetsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this ListAssetsRequest.

        开发者应用作为资产权属的可选字段。

        :param x_app_user_id: The x_app_user_id of this ListAssetsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def limit(self):
        """Gets the limit of this ListAssetsRequest.

        每页显示的条目数量。

        :return: The limit of this ListAssetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAssetsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListAssetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAssetsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListAssetsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAssetsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListAssetsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        """Gets the name of this ListAssetsRequest.

        按名称模糊查询。

        :return: The name of this ListAssetsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAssetsRequest.

        按名称模糊查询。

        :param name: The name of this ListAssetsRequest.
        :type name: str
        """
        self._name = name

    @property
    def tag(self):
        """Gets the tag of this ListAssetsRequest.

        按标签模糊查询。

        :return: The tag of this ListAssetsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListAssetsRequest.

        按标签模糊查询。

        :param tag: The tag of this ListAssetsRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def start_time(self):
        """Gets the start_time of this ListAssetsRequest.

        起始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The start_time of this ListAssetsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListAssetsRequest.

        起始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param start_time: The start_time of this ListAssetsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAssetsRequest.

        结束时间。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"。

        :return: The end_time of this ListAssetsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAssetsRequest.

        结束时间。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"。

        :param end_time: The end_time of this ListAssetsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def asset_type(self):
        """Gets the asset_type of this ListAssetsRequest.

        资产类型。多个类型使用英文逗号分割。 * HUMAN_MODEL：数字人模型 * VOICE_MODEL：音色模型（仅系统管理员可上传） * SCENE：场景模型 * ANIMATION：动作动画 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * HUMAN_MODEL_2D: 2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐

        :return: The asset_type of this ListAssetsRequest.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this ListAssetsRequest.

        资产类型。多个类型使用英文逗号分割。 * HUMAN_MODEL：数字人模型 * VOICE_MODEL：音色模型（仅系统管理员可上传） * SCENE：场景模型 * ANIMATION：动作动画 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * HUMAN_MODEL_2D: 2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐

        :param asset_type: The asset_type of this ListAssetsRequest.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def sort_key(self):
        """Gets the sort_key of this ListAssetsRequest.

        排序字段，目前只支持create_time。

        :return: The sort_key of this ListAssetsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListAssetsRequest.

        排序字段，目前只支持create_time。

        :param sort_key: The sort_key of this ListAssetsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListAssetsRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :return: The sort_dir of this ListAssetsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListAssetsRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :param sort_dir: The sort_dir of this ListAssetsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def asset_source(self):
        """Gets the asset_source of this ListAssetsRequest.

        资产来源。 * SYSTEM：系统资产 * CUSTOMIZATION：租户资产 * ALL：所有资产  默认查询租户资产。

        :return: The asset_source of this ListAssetsRequest.
        :rtype: str
        """
        return self._asset_source

    @asset_source.setter
    def asset_source(self, asset_source):
        """Sets the asset_source of this ListAssetsRequest.

        资产来源。 * SYSTEM：系统资产 * CUSTOMIZATION：租户资产 * ALL：所有资产  默认查询租户资产。

        :param asset_source: The asset_source of this ListAssetsRequest.
        :type asset_source: str
        """
        self._asset_source = asset_source

    @property
    def asset_state(self):
        """Gets the asset_state of this ListAssetsRequest.

        资产状态。多个资产状态使用英文逗号分割。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK：资产被冻结，资产不可用，不可查看文件。 默认查询所有状态的资产。

        :return: The asset_state of this ListAssetsRequest.
        :rtype: str
        """
        return self._asset_state

    @asset_state.setter
    def asset_state(self, asset_state):
        """Sets the asset_state of this ListAssetsRequest.

        资产状态。多个资产状态使用英文逗号分割。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK：资产被冻结，资产不可用，不可查看文件。 默认查询所有状态的资产。

        :param asset_state: The asset_state of this ListAssetsRequest.
        :type asset_state: str
        """
        self._asset_state = asset_state

    @property
    def style_id(self):
        """Gets the style_id of this ListAssetsRequest.

        基于风格化ID查询关联资产。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02  * system_female_002：女性风格02

        :return: The style_id of this ListAssetsRequest.
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        """Sets the style_id of this ListAssetsRequest.

        基于风格化ID查询关联资产。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02  * system_female_002：女性风格02

        :param style_id: The style_id of this ListAssetsRequest.
        :type style_id: str
        """
        self._style_id = style_id

    @property
    def render_engine(self):
        """Gets the render_engine of this ListAssetsRequest.

        可用引擎。 * UE：UE引擎 * MetaEngine：MetaEngine引擎 > 该字段当前只对MetaEngine白名单用户生效

        :return: The render_engine of this ListAssetsRequest.
        :rtype: str
        """
        return self._render_engine

    @render_engine.setter
    def render_engine(self, render_engine):
        """Sets the render_engine of this ListAssetsRequest.

        可用引擎。 * UE：UE引擎 * MetaEngine：MetaEngine引擎 > 该字段当前只对MetaEngine白名单用户生效

        :param render_engine: The render_engine of this ListAssetsRequest.
        :type render_engine: str
        """
        self._render_engine = render_engine

    @property
    def sex(self):
        """Gets the sex of this ListAssetsRequest.

        性别。多选使用英文逗号分隔。

        :return: The sex of this ListAssetsRequest.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this ListAssetsRequest.

        性别。多选使用英文逗号分隔。

        :param sex: The sex of this ListAssetsRequest.
        :type sex: str
        """
        self._sex = sex

    @property
    def language(self):
        """Gets the language of this ListAssetsRequest.

        语言。多选使用英文逗号分隔。

        :return: The language of this ListAssetsRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ListAssetsRequest.

        语言。多选使用英文逗号分隔。

        :param language: The language of this ListAssetsRequest.
        :type language: str
        """
        self._language = language

    @property
    def system_property(self):
        """Gets the system_property of this ListAssetsRequest.

        系统属性。  key和value间用\":\"分隔，多个key之间用\",\"分隔。  如system_property=BACKGROUND_IMG:Yes,RENDER_ENGINE:MetaEngine。  不同Key对应Value取值如下： * STYLE_ID：风格Id * RENDER_ENGINE：引擎类型，可取值UE或MetaEngine * BACKGROUND_IMG：视频制作的2D背景图片，可取值Yes * BACKGROUND_SCENE：视频制作的2D背景场景，可取值Horizontal（横屏）或者Vertical（竖屏） * CREATED_BY_PLATFORM：是否平台生成，可取值Yes

        :return: The system_property of this ListAssetsRequest.
        :rtype: str
        """
        return self._system_property

    @system_property.setter
    def system_property(self, system_property):
        """Sets the system_property of this ListAssetsRequest.

        系统属性。  key和value间用\":\"分隔，多个key之间用\",\"分隔。  如system_property=BACKGROUND_IMG:Yes,RENDER_ENGINE:MetaEngine。  不同Key对应Value取值如下： * STYLE_ID：风格Id * RENDER_ENGINE：引擎类型，可取值UE或MetaEngine * BACKGROUND_IMG：视频制作的2D背景图片，可取值Yes * BACKGROUND_SCENE：视频制作的2D背景场景，可取值Horizontal（横屏）或者Vertical（竖屏） * CREATED_BY_PLATFORM：是否平台生成，可取值Yes

        :param system_property: The system_property of this ListAssetsRequest.
        :type system_property: str
        """
        self._system_property = system_property

    @property
    def action_editable(self):
        """Gets the action_editable of this ListAssetsRequest.

        动作是否可编辑。仅在分身数字人模型查询时有效。

        :return: The action_editable of this ListAssetsRequest.
        :rtype: bool
        """
        return self._action_editable

    @action_editable.setter
    def action_editable(self, action_editable):
        """Sets the action_editable of this ListAssetsRequest.

        动作是否可编辑。仅在分身数字人模型查询时有效。

        :param action_editable: The action_editable of this ListAssetsRequest.
        :type action_editable: bool
        """
        self._action_editable = action_editable

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
