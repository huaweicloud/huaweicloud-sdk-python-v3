# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'asset_model_id': 'str',
        'asset_model_name': 'str',
        'name': 'str',
        'display_name': 'str',
        'properties': 'list[PropertyResponse]',
        'analyses': 'list[AnalysisResponse]',
        'root': 'str',
        'parent': 'str',
        'children': 'list[str]',
        'state': 'str',
        'publish_state': 'str',
        'created_time': 'str',
        'modified_time': 'str',
        'published_time': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_model_id': 'asset_model_id',
        'asset_model_name': 'asset_model_name',
        'name': 'name',
        'display_name': 'display_name',
        'properties': 'properties',
        'analyses': 'analyses',
        'root': 'root',
        'parent': 'parent',
        'children': 'children',
        'state': 'state',
        'publish_state': 'publish_state',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'published_time': 'published_time'
    }

    def __init__(self, asset_id=None, asset_model_id=None, asset_model_name=None, name=None, display_name=None, properties=None, analyses=None, root=None, parent=None, children=None, state=None, publish_state=None, created_time=None, modified_time=None, published_time=None):
        r"""AssetResponse

        The model defined in huaweicloud sdk

        :param asset_id: 资产ID
        :type asset_id: str
        :param asset_model_id: 资产模型ID
        :type asset_model_id: str
        :param asset_model_name: 资产模型名称
        :type asset_model_name: str
        :param name: 资产名称
        :type name: str
        :param display_name: 资产显示名称
        :type display_name: str
        :param properties: 属性集
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyResponse`]
        :param analyses: 分析任务集
        :type analyses: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisResponse`]
        :param root: 根资产ID
        :type root: str
        :param parent: 父资产ID，根资产的父资产ID为null
        :type parent: str
        :param children: 子资产ID集
        :type children: list[str]
        :param state: 资产状态，正常状态（ACTIVE），异常状态（INACTIVE）；只有草稿态（SKETCH）资产有此状态；资产处于异常状态的场景有：1、该资产存在未填写设备ID的测量数据类别的属性；2、该资产存在未填写静态值的静态配置类别的属性；3、该资产存在分析任务，该分析任务的输入参数存在属性引用类型为引用其他资产属性，且没有为该输入参数配置引用的其他资产的资产ID
        :type state: str
        :param publish_state: 资产发布状态，发布中（PUBLISHING），发布完成（PUBLISHED）；只能对草稿态（SKETCH）的根资产进行发布，也只有草稿态的根资产有此字段；如果根资产从未发布过则值为null
        :type publish_state: str
        :param created_time: 创建时间，格式\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;\&quot;
        :type created_time: str
        :param modified_time: 修改时间，格式\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;\&quot;
        :type modified_time: str
        :param published_time: 发布时间，只能对草稿态（SKETCH）的根资产进行发布，也只有草稿态的根资产有此字段；如果从未发布过则值为null；格式\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;\&quot;
        :type published_time: str
        """
        
        

        self._asset_id = None
        self._asset_model_id = None
        self._asset_model_name = None
        self._name = None
        self._display_name = None
        self._properties = None
        self._analyses = None
        self._root = None
        self._parent = None
        self._children = None
        self._state = None
        self._publish_state = None
        self._created_time = None
        self._modified_time = None
        self._published_time = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if asset_model_id is not None:
            self.asset_model_id = asset_model_id
        if asset_model_name is not None:
            self.asset_model_name = asset_model_name
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if properties is not None:
            self.properties = properties
        if analyses is not None:
            self.analyses = analyses
        if root is not None:
            self.root = root
        if parent is not None:
            self.parent = parent
        if children is not None:
            self.children = children
        if state is not None:
            self.state = state
        if publish_state is not None:
            self.publish_state = publish_state
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if published_time is not None:
            self.published_time = published_time

    @property
    def asset_id(self):
        r"""Gets the asset_id of this AssetResponse.

        资产ID

        :return: The asset_id of this AssetResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this AssetResponse.

        资产ID

        :param asset_id: The asset_id of this AssetResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_model_id(self):
        r"""Gets the asset_model_id of this AssetResponse.

        资产模型ID

        :return: The asset_model_id of this AssetResponse.
        :rtype: str
        """
        return self._asset_model_id

    @asset_model_id.setter
    def asset_model_id(self, asset_model_id):
        r"""Sets the asset_model_id of this AssetResponse.

        资产模型ID

        :param asset_model_id: The asset_model_id of this AssetResponse.
        :type asset_model_id: str
        """
        self._asset_model_id = asset_model_id

    @property
    def asset_model_name(self):
        r"""Gets the asset_model_name of this AssetResponse.

        资产模型名称

        :return: The asset_model_name of this AssetResponse.
        :rtype: str
        """
        return self._asset_model_name

    @asset_model_name.setter
    def asset_model_name(self, asset_model_name):
        r"""Sets the asset_model_name of this AssetResponse.

        资产模型名称

        :param asset_model_name: The asset_model_name of this AssetResponse.
        :type asset_model_name: str
        """
        self._asset_model_name = asset_model_name

    @property
    def name(self):
        r"""Gets the name of this AssetResponse.

        资产名称

        :return: The name of this AssetResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AssetResponse.

        资产名称

        :param name: The name of this AssetResponse.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this AssetResponse.

        资产显示名称

        :return: The display_name of this AssetResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this AssetResponse.

        资产显示名称

        :param display_name: The display_name of this AssetResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def properties(self):
        r"""Gets the properties of this AssetResponse.

        属性集

        :return: The properties of this AssetResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyResponse`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this AssetResponse.

        属性集

        :param properties: The properties of this AssetResponse.
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyResponse`]
        """
        self._properties = properties

    @property
    def analyses(self):
        r"""Gets the analyses of this AssetResponse.

        分析任务集

        :return: The analyses of this AssetResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisResponse`]
        """
        return self._analyses

    @analyses.setter
    def analyses(self, analyses):
        r"""Sets the analyses of this AssetResponse.

        分析任务集

        :param analyses: The analyses of this AssetResponse.
        :type analyses: list[:class:`huaweicloudsdkiotanalytics.v1.AnalysisResponse`]
        """
        self._analyses = analyses

    @property
    def root(self):
        r"""Gets the root of this AssetResponse.

        根资产ID

        :return: The root of this AssetResponse.
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        r"""Sets the root of this AssetResponse.

        根资产ID

        :param root: The root of this AssetResponse.
        :type root: str
        """
        self._root = root

    @property
    def parent(self):
        r"""Gets the parent of this AssetResponse.

        父资产ID，根资产的父资产ID为null

        :return: The parent of this AssetResponse.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        r"""Sets the parent of this AssetResponse.

        父资产ID，根资产的父资产ID为null

        :param parent: The parent of this AssetResponse.
        :type parent: str
        """
        self._parent = parent

    @property
    def children(self):
        r"""Gets the children of this AssetResponse.

        子资产ID集

        :return: The children of this AssetResponse.
        :rtype: list[str]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this AssetResponse.

        子资产ID集

        :param children: The children of this AssetResponse.
        :type children: list[str]
        """
        self._children = children

    @property
    def state(self):
        r"""Gets the state of this AssetResponse.

        资产状态，正常状态（ACTIVE），异常状态（INACTIVE）；只有草稿态（SKETCH）资产有此状态；资产处于异常状态的场景有：1、该资产存在未填写设备ID的测量数据类别的属性；2、该资产存在未填写静态值的静态配置类别的属性；3、该资产存在分析任务，该分析任务的输入参数存在属性引用类型为引用其他资产属性，且没有为该输入参数配置引用的其他资产的资产ID

        :return: The state of this AssetResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this AssetResponse.

        资产状态，正常状态（ACTIVE），异常状态（INACTIVE）；只有草稿态（SKETCH）资产有此状态；资产处于异常状态的场景有：1、该资产存在未填写设备ID的测量数据类别的属性；2、该资产存在未填写静态值的静态配置类别的属性；3、该资产存在分析任务，该分析任务的输入参数存在属性引用类型为引用其他资产属性，且没有为该输入参数配置引用的其他资产的资产ID

        :param state: The state of this AssetResponse.
        :type state: str
        """
        self._state = state

    @property
    def publish_state(self):
        r"""Gets the publish_state of this AssetResponse.

        资产发布状态，发布中（PUBLISHING），发布完成（PUBLISHED）；只能对草稿态（SKETCH）的根资产进行发布，也只有草稿态的根资产有此字段；如果根资产从未发布过则值为null

        :return: The publish_state of this AssetResponse.
        :rtype: str
        """
        return self._publish_state

    @publish_state.setter
    def publish_state(self, publish_state):
        r"""Sets the publish_state of this AssetResponse.

        资产发布状态，发布中（PUBLISHING），发布完成（PUBLISHED）；只能对草稿态（SKETCH）的根资产进行发布，也只有草稿态的根资产有此字段；如果根资产从未发布过则值为null

        :param publish_state: The publish_state of this AssetResponse.
        :type publish_state: str
        """
        self._publish_state = publish_state

    @property
    def created_time(self):
        r"""Gets the created_time of this AssetResponse.

        创建时间，格式\"yyyy-MM-dd'T'HH:mm:ss'Z'\"

        :return: The created_time of this AssetResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this AssetResponse.

        创建时间，格式\"yyyy-MM-dd'T'HH:mm:ss'Z'\"

        :param created_time: The created_time of this AssetResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this AssetResponse.

        修改时间，格式\"yyyy-MM-dd'T'HH:mm:ss'Z'\"

        :return: The modified_time of this AssetResponse.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this AssetResponse.

        修改时间，格式\"yyyy-MM-dd'T'HH:mm:ss'Z'\"

        :param modified_time: The modified_time of this AssetResponse.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def published_time(self):
        r"""Gets the published_time of this AssetResponse.

        发布时间，只能对草稿态（SKETCH）的根资产进行发布，也只有草稿态的根资产有此字段；如果从未发布过则值为null；格式\"yyyy-MM-dd'T'HH:mm:ss'Z'\"

        :return: The published_time of this AssetResponse.
        :rtype: str
        """
        return self._published_time

    @published_time.setter
    def published_time(self, published_time):
        r"""Sets the published_time of this AssetResponse.

        发布时间，只能对草稿态（SKETCH）的根资产进行发布，也只有草稿态的根资产有此字段；如果从未发布过则值为null；格式\"yyyy-MM-dd'T'HH:mm:ss'Z'\"

        :param published_time: The published_time of this AssetResponse.
        :type published_time: str
        """
        self._published_time = published_time

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
        if not isinstance(other, AssetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
