# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentEnvironment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor_type': 'str',
        'domain_id': 'str',
        'region_id': 'str',
        'cross_workspace_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'vendor_type': 'vendor_type',
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'cross_workspace_id': 'cross_workspace_id',
        'project_id': 'project_id'
    }

    def __init__(self, vendor_type=None, domain_id=None, region_id=None, cross_workspace_id=None, project_id=None):
        r"""IncidentEnvironment

        The model defined in huaweicloud sdk

        :param vendor_type: 环境供应商
        :type vendor_type: str
        :param domain_id: 租户id
        :type domain_id: str
        :param region_id: 区域id，全局服务global
        :type region_id: str
        :param cross_workspace_id: 数据投递前的源工作空间id，在源空间下值为null，投递后为被委托用户的id
        :type cross_workspace_id: str
        :param project_id: 项目id， 全局服务默认null
        :type project_id: str
        """
        
        

        self._vendor_type = None
        self._domain_id = None
        self._region_id = None
        self._cross_workspace_id = None
        self._project_id = None
        self.discriminator = None

        if vendor_type is not None:
            self.vendor_type = vendor_type
        if domain_id is not None:
            self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if cross_workspace_id is not None:
            self.cross_workspace_id = cross_workspace_id
        if project_id is not None:
            self.project_id = project_id

    @property
    def vendor_type(self):
        r"""Gets the vendor_type of this IncidentEnvironment.

        环境供应商

        :return: The vendor_type of this IncidentEnvironment.
        :rtype: str
        """
        return self._vendor_type

    @vendor_type.setter
    def vendor_type(self, vendor_type):
        r"""Sets the vendor_type of this IncidentEnvironment.

        环境供应商

        :param vendor_type: The vendor_type of this IncidentEnvironment.
        :type vendor_type: str
        """
        self._vendor_type = vendor_type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this IncidentEnvironment.

        租户id

        :return: The domain_id of this IncidentEnvironment.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this IncidentEnvironment.

        租户id

        :param domain_id: The domain_id of this IncidentEnvironment.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this IncidentEnvironment.

        区域id，全局服务global

        :return: The region_id of this IncidentEnvironment.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this IncidentEnvironment.

        区域id，全局服务global

        :param region_id: The region_id of this IncidentEnvironment.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def cross_workspace_id(self):
        r"""Gets the cross_workspace_id of this IncidentEnvironment.

        数据投递前的源工作空间id，在源空间下值为null，投递后为被委托用户的id

        :return: The cross_workspace_id of this IncidentEnvironment.
        :rtype: str
        """
        return self._cross_workspace_id

    @cross_workspace_id.setter
    def cross_workspace_id(self, cross_workspace_id):
        r"""Sets the cross_workspace_id of this IncidentEnvironment.

        数据投递前的源工作空间id，在源空间下值为null，投递后为被委托用户的id

        :param cross_workspace_id: The cross_workspace_id of this IncidentEnvironment.
        :type cross_workspace_id: str
        """
        self._cross_workspace_id = cross_workspace_id

    @property
    def project_id(self):
        r"""Gets the project_id of this IncidentEnvironment.

        项目id， 全局服务默认null

        :return: The project_id of this IncidentEnvironment.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this IncidentEnvironment.

        项目id， 全局服务默认null

        :param project_id: The project_id of this IncidentEnvironment.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, IncidentEnvironment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
