# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MeshSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'type': 'str',
        'version': 'str',
        'extend_params': 'MeshExtendParams'
    }

    attribute_map = {
        'region': 'region',
        'type': 'type',
        'version': 'version',
        'extend_params': 'extendParams'
    }

    def __init__(self, region=None, type=None, version=None, extend_params=None):
        """MeshSpec

        The model defined in huaweicloud sdk

        :param region: 网格控制面组件所在的region。 创建企业版网格时需要填写该参数，选择控制面组件所在的region； 创建基础版时网格组件安装在用户所提供的集群中，不需要填写该参数。
        :type region: str
        :param type: 网格类型：  Managed：企业版网格  InCluster：基础版网格
        :type type: str
        :param version: 网格版本
        :type version: str
        :param extend_params: 
        :type extend_params: :class:`huaweicloudsdkasm.v1.MeshExtendParams`
        """
        
        

        self._region = None
        self._type = None
        self._version = None
        self._extend_params = None
        self.discriminator = None

        if region is not None:
            self.region = region
        self.type = type
        self.version = version
        if extend_params is not None:
            self.extend_params = extend_params

    @property
    def region(self):
        """Gets the region of this MeshSpec.

        网格控制面组件所在的region。 创建企业版网格时需要填写该参数，选择控制面组件所在的region； 创建基础版时网格组件安装在用户所提供的集群中，不需要填写该参数。

        :return: The region of this MeshSpec.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this MeshSpec.

        网格控制面组件所在的region。 创建企业版网格时需要填写该参数，选择控制面组件所在的region； 创建基础版时网格组件安装在用户所提供的集群中，不需要填写该参数。

        :param region: The region of this MeshSpec.
        :type region: str
        """
        self._region = region

    @property
    def type(self):
        """Gets the type of this MeshSpec.

        网格类型：  Managed：企业版网格  InCluster：基础版网格

        :return: The type of this MeshSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MeshSpec.

        网格类型：  Managed：企业版网格  InCluster：基础版网格

        :param type: The type of this MeshSpec.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this MeshSpec.

        网格版本

        :return: The version of this MeshSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MeshSpec.

        网格版本

        :param version: The version of this MeshSpec.
        :type version: str
        """
        self._version = version

    @property
    def extend_params(self):
        """Gets the extend_params of this MeshSpec.

        :return: The extend_params of this MeshSpec.
        :rtype: :class:`huaweicloudsdkasm.v1.MeshExtendParams`
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        """Sets the extend_params of this MeshSpec.

        :param extend_params: The extend_params of this MeshSpec.
        :type extend_params: :class:`huaweicloudsdkasm.v1.MeshExtendParams`
        """
        self._extend_params = extend_params

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
        if not isinstance(other, MeshSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
