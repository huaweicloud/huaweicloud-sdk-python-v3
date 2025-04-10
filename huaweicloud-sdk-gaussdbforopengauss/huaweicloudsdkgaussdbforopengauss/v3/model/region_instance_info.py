# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegionInstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'region_code': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'region_code': 'region_code',
        'ip_address': 'ip_address'
    }

    def __init__(self, instance_id=None, project_id=None, project_name=None, region_code=None, ip_address=None):
        r"""RegionInstanceInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例id。
        :type instance_id: str
        :param project_id: 实例项目id。
        :type project_id: str
        :param project_name: 实例项目名称。
        :type project_name: str
        :param region_code: regionCode编码。
        :type region_code: str
        :param ip_address: 数据ip地址列表“,”分割。
        :type ip_address: str
        """
        
        

        self._instance_id = None
        self._project_id = None
        self._project_name = None
        self._region_code = None
        self._ip_address = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if region_code is not None:
            self.region_code = region_code
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RegionInstanceInfo.

        实例id。

        :return: The instance_id of this RegionInstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RegionInstanceInfo.

        实例id。

        :param instance_id: The instance_id of this RegionInstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        r"""Gets the project_id of this RegionInstanceInfo.

        实例项目id。

        :return: The project_id of this RegionInstanceInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RegionInstanceInfo.

        实例项目id。

        :param project_id: The project_id of this RegionInstanceInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this RegionInstanceInfo.

        实例项目名称。

        :return: The project_name of this RegionInstanceInfo.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this RegionInstanceInfo.

        实例项目名称。

        :param project_name: The project_name of this RegionInstanceInfo.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def region_code(self):
        r"""Gets the region_code of this RegionInstanceInfo.

        regionCode编码。

        :return: The region_code of this RegionInstanceInfo.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this RegionInstanceInfo.

        regionCode编码。

        :param region_code: The region_code of this RegionInstanceInfo.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def ip_address(self):
        r"""Gets the ip_address of this RegionInstanceInfo.

        数据ip地址列表“,”分割。

        :return: The ip_address of this RegionInstanceInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this RegionInstanceInfo.

        数据ip地址列表“,”分割。

        :param ip_address: The ip_address of this RegionInstanceInfo.
        :type ip_address: str
        """
        self._ip_address = ip_address

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
        if not isinstance(other, RegionInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
