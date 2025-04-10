# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'uid': 'str',
        'alias': 'str',
        'annotations': 'dict(str, str)',
        'labels': 'dict(str, str)',
        'creation_timestamp': 'str',
        'update_timestamp': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'alias': 'alias',
        'annotations': 'annotations',
        'labels': 'labels',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp'
    }

    def __init__(self, name=None, uid=None, alias=None, annotations=None, labels=None, creation_timestamp=None, update_timestamp=None):
        r"""ClusterMetadata

        The model defined in huaweicloud sdk

        :param name: 集群名称。  命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-128位，且不能以中划线(-)结尾。
        :type name: str
        :param uid: 集群ID，资源唯一标识，创建成功后自动生成，填写无效。在创建包周期集群时，响应体不返回集群ID。
        :type uid: str
        :param alias: 集群显示名，用于在 CCE 界面显示，该名称创建后可修改。  命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-128位，且不能以中划线(-)结尾。  显示名和其他集群的名称、显示名不可以重复。  在创建集群、更新集群请求体中，集群显示名alias未指定或取值为空，表示与集群名称name一致。在查询集群等响应体中，集群显示名alias将必然返回，未配置时将返回集群名称name。
        :type alias: str
        :param annotations: 集群注解，由key/value组成：  &#x60;&#x60;&#x60; \&quot;annotations\&quot;: {    \&quot;key1\&quot; : \&quot;value1\&quot;,    \&quot;key2\&quot; : \&quot;value2\&quot; } &#x60;&#x60;&#x60;  &gt;    - Annotations不用于标识和选择对象。Annotations中的元数据可以是small或large，structured或unstructured，并且可以包括标签不允许使用的字符。 &gt;    - 该字段不会被数据库保存，当前仅用于指定集群待安装插件。 &gt;    - 可通过加入\&quot;cluster.install.addons.external/install\&quot;:\&quot;[{\&quot;addonTemplateName\&quot;:\&quot;icagent\&quot;}]\&quot;的键值对在创建集群时安装ICAgent。 
        :type annotations: dict(str, str)
        :param labels: 集群标签，key/value对格式。  &gt;  该字段值由系统自动生成，用于升级时前端识别集群支持的特性开关，用户指定无效。
        :type labels: dict(str, str)
        :param creation_timestamp: 集群创建时间
        :type creation_timestamp: str
        :param update_timestamp: 集群更新时间
        :type update_timestamp: str
        """
        
        

        self._name = None
        self._uid = None
        self._alias = None
        self._annotations = None
        self._labels = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self.discriminator = None

        self.name = name
        if uid is not None:
            self.uid = uid
        if alias is not None:
            self.alias = alias
        if annotations is not None:
            self.annotations = annotations
        if labels is not None:
            self.labels = labels
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp

    @property
    def name(self):
        r"""Gets the name of this ClusterMetadata.

        集群名称。  命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-128位，且不能以中划线(-)结尾。

        :return: The name of this ClusterMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ClusterMetadata.

        集群名称。  命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-128位，且不能以中划线(-)结尾。

        :param name: The name of this ClusterMetadata.
        :type name: str
        """
        self._name = name

    @property
    def uid(self):
        r"""Gets the uid of this ClusterMetadata.

        集群ID，资源唯一标识，创建成功后自动生成，填写无效。在创建包周期集群时，响应体不返回集群ID。

        :return: The uid of this ClusterMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this ClusterMetadata.

        集群ID，资源唯一标识，创建成功后自动生成，填写无效。在创建包周期集群时，响应体不返回集群ID。

        :param uid: The uid of this ClusterMetadata.
        :type uid: str
        """
        self._uid = uid

    @property
    def alias(self):
        r"""Gets the alias of this ClusterMetadata.

        集群显示名，用于在 CCE 界面显示，该名称创建后可修改。  命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-128位，且不能以中划线(-)结尾。  显示名和其他集群的名称、显示名不可以重复。  在创建集群、更新集群请求体中，集群显示名alias未指定或取值为空，表示与集群名称name一致。在查询集群等响应体中，集群显示名alias将必然返回，未配置时将返回集群名称name。

        :return: The alias of this ClusterMetadata.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this ClusterMetadata.

        集群显示名，用于在 CCE 界面显示，该名称创建后可修改。  命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-128位，且不能以中划线(-)结尾。  显示名和其他集群的名称、显示名不可以重复。  在创建集群、更新集群请求体中，集群显示名alias未指定或取值为空，表示与集群名称name一致。在查询集群等响应体中，集群显示名alias将必然返回，未配置时将返回集群名称name。

        :param alias: The alias of this ClusterMetadata.
        :type alias: str
        """
        self._alias = alias

    @property
    def annotations(self):
        r"""Gets the annotations of this ClusterMetadata.

        集群注解，由key/value组成：  ``` \"annotations\": {    \"key1\" : \"value1\",    \"key2\" : \"value2\" } ```  >    - Annotations不用于标识和选择对象。Annotations中的元数据可以是small或large，structured或unstructured，并且可以包括标签不允许使用的字符。 >    - 该字段不会被数据库保存，当前仅用于指定集群待安装插件。 >    - 可通过加入\"cluster.install.addons.external/install\":\"[{\"addonTemplateName\":\"icagent\"}]\"的键值对在创建集群时安装ICAgent。 

        :return: The annotations of this ClusterMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this ClusterMetadata.

        集群注解，由key/value组成：  ``` \"annotations\": {    \"key1\" : \"value1\",    \"key2\" : \"value2\" } ```  >    - Annotations不用于标识和选择对象。Annotations中的元数据可以是small或large，structured或unstructured，并且可以包括标签不允许使用的字符。 >    - 该字段不会被数据库保存，当前仅用于指定集群待安装插件。 >    - 可通过加入\"cluster.install.addons.external/install\":\"[{\"addonTemplateName\":\"icagent\"}]\"的键值对在创建集群时安装ICAgent。 

        :param annotations: The annotations of this ClusterMetadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def labels(self):
        r"""Gets the labels of this ClusterMetadata.

        集群标签，key/value对格式。  >  该字段值由系统自动生成，用于升级时前端识别集群支持的特性开关，用户指定无效。

        :return: The labels of this ClusterMetadata.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ClusterMetadata.

        集群标签，key/value对格式。  >  该字段值由系统自动生成，用于升级时前端识别集群支持的特性开关，用户指定无效。

        :param labels: The labels of this ClusterMetadata.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this ClusterMetadata.

        集群创建时间

        :return: The creation_timestamp of this ClusterMetadata.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this ClusterMetadata.

        集群创建时间

        :param creation_timestamp: The creation_timestamp of this ClusterMetadata.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        r"""Gets the update_timestamp of this ClusterMetadata.

        集群更新时间

        :return: The update_timestamp of this ClusterMetadata.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        r"""Sets the update_timestamp of this ClusterMetadata.

        集群更新时间

        :param update_timestamp: The update_timestamp of this ClusterMetadata.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

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
        if not isinstance(other, ClusterMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
