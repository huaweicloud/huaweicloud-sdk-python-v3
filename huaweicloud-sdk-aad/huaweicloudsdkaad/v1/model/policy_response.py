# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'package_id': 'str',
        'package_name': 'str',
        'name': 'str',
        'description': 'str',
        'region': 'str',
        'clean_threshold': 'int',
        'num_protected_ip': 'int'
    }

    attribute_map = {
        'id': 'id',
        'package_id': 'package_id',
        'package_name': 'package_name',
        'name': 'name',
        'description': 'description',
        'region': 'region',
        'clean_threshold': 'clean_threshold',
        'num_protected_ip': 'num_protected_ip'
    }

    def __init__(self, id=None, package_id=None, package_name=None, name=None, description=None, region=None, clean_threshold=None, num_protected_ip=None):
        """PolicyResponse

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param package_id: 防护包id
        :type package_id: str
        :param package_name: 防护包名
        :type package_name: str
        :param name: 策略名
        :type name: str
        :param description: 描述
        :type description: str
        :param region: 所属region的id
        :type region: str
        :param clean_threshold: 清洗阈值
        :type clean_threshold: int
        :param num_protected_ip: 防护ip数
        :type num_protected_ip: int
        """
        
        

        self._id = None
        self._package_id = None
        self._package_name = None
        self._name = None
        self._description = None
        self._region = None
        self._clean_threshold = None
        self._num_protected_ip = None
        self.discriminator = None

        self.id = id
        self.package_id = package_id
        self.package_name = package_name
        self.name = name
        self.description = description
        self.region = region
        self.clean_threshold = clean_threshold
        self.num_protected_ip = num_protected_ip

    @property
    def id(self):
        """Gets the id of this PolicyResponse.

        id

        :return: The id of this PolicyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyResponse.

        id

        :param id: The id of this PolicyResponse.
        :type id: str
        """
        self._id = id

    @property
    def package_id(self):
        """Gets the package_id of this PolicyResponse.

        防护包id

        :return: The package_id of this PolicyResponse.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this PolicyResponse.

        防护包id

        :param package_id: The package_id of this PolicyResponse.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def package_name(self):
        """Gets the package_name of this PolicyResponse.

        防护包名

        :return: The package_name of this PolicyResponse.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this PolicyResponse.

        防护包名

        :param package_name: The package_name of this PolicyResponse.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def name(self):
        """Gets the name of this PolicyResponse.

        策略名

        :return: The name of this PolicyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyResponse.

        策略名

        :param name: The name of this PolicyResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PolicyResponse.

        描述

        :return: The description of this PolicyResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyResponse.

        描述

        :param description: The description of this PolicyResponse.
        :type description: str
        """
        self._description = description

    @property
    def region(self):
        """Gets the region of this PolicyResponse.

        所属region的id

        :return: The region of this PolicyResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this PolicyResponse.

        所属region的id

        :param region: The region of this PolicyResponse.
        :type region: str
        """
        self._region = region

    @property
    def clean_threshold(self):
        """Gets the clean_threshold of this PolicyResponse.

        清洗阈值

        :return: The clean_threshold of this PolicyResponse.
        :rtype: int
        """
        return self._clean_threshold

    @clean_threshold.setter
    def clean_threshold(self, clean_threshold):
        """Sets the clean_threshold of this PolicyResponse.

        清洗阈值

        :param clean_threshold: The clean_threshold of this PolicyResponse.
        :type clean_threshold: int
        """
        self._clean_threshold = clean_threshold

    @property
    def num_protected_ip(self):
        """Gets the num_protected_ip of this PolicyResponse.

        防护ip数

        :return: The num_protected_ip of this PolicyResponse.
        :rtype: int
        """
        return self._num_protected_ip

    @num_protected_ip.setter
    def num_protected_ip(self, num_protected_ip):
        """Sets the num_protected_ip of this PolicyResponse.

        防护ip数

        :param num_protected_ip: The num_protected_ip of this PolicyResponse.
        :type num_protected_ip: int
        """
        self._num_protected_ip = num_protected_ip

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
        if not isinstance(other, PolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
