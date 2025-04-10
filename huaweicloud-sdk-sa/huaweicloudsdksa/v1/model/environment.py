# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Environment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'region_id': 'region_id'
    }

    def __init__(self, type=None, domain_id=None, project_id=None, region_id=None):
        r"""Environment

        The model defined in huaweicloud sdk

        :param type: 环境供应商，HWCP/HWC/AWS/Azure/GCP等。
        :type type: str
        :param domain_id: 租户账号ID，用来标识事件所属租户。
        :type domain_id: str
        :param project_id: 租户项目ID，用来标识事件所属项目区域。
        :type project_id: str
        :param region_id: 数据源产品所在区域，具体取值范围查看华为云地区和终端节点定义。
        :type region_id: str
        """
        
        

        self._type = None
        self._domain_id = None
        self._project_id = None
        self._region_id = None
        self.discriminator = None

        self.type = type
        self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id

    @property
    def type(self):
        r"""Gets the type of this Environment.

        环境供应商，HWCP/HWC/AWS/Azure/GCP等。

        :return: The type of this Environment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Environment.

        环境供应商，HWCP/HWC/AWS/Azure/GCP等。

        :param type: The type of this Environment.
        :type type: str
        """
        self._type = type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this Environment.

        租户账号ID，用来标识事件所属租户。

        :return: The domain_id of this Environment.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this Environment.

        租户账号ID，用来标识事件所属租户。

        :param domain_id: The domain_id of this Environment.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this Environment.

        租户项目ID，用来标识事件所属项目区域。

        :return: The project_id of this Environment.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Environment.

        租户项目ID，用来标识事件所属项目区域。

        :param project_id: The project_id of this Environment.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this Environment.

        数据源产品所在区域，具体取值范围查看华为云地区和终端节点定义。

        :return: The region_id of this Environment.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this Environment.

        数据源产品所在区域，具体取值范围查看华为云地区和终端节点定义。

        :param region_id: The region_id of this Environment.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, Environment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
