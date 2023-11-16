# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePolicyResponse(SdkResponse):

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
        'name': 'str',
        'package_id': 'str',
        'description': 'str',
        'clean_threshold': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'package_id': 'package_id',
        'description': 'description',
        'clean_threshold': 'clean_threshold'
    }

    def __init__(self, id=None, name=None, package_id=None, description=None, clean_threshold=None):
        """CreatePolicyResponse

        The model defined in huaweicloud sdk

        :param id: 策略id
        :type id: str
        :param name: 策略名
        :type name: str
        :param package_id: 防护包id
        :type package_id: str
        :param description: 描述
        :type description: str
        :param clean_threshold: 清洗阈值
        :type clean_threshold: int
        """
        
        super(CreatePolicyResponse, self).__init__()

        self._id = None
        self._name = None
        self._package_id = None
        self._description = None
        self._clean_threshold = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if package_id is not None:
            self.package_id = package_id
        if description is not None:
            self.description = description
        if clean_threshold is not None:
            self.clean_threshold = clean_threshold

    @property
    def id(self):
        """Gets the id of this CreatePolicyResponse.

        策略id

        :return: The id of this CreatePolicyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatePolicyResponse.

        策略id

        :param id: The id of this CreatePolicyResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreatePolicyResponse.

        策略名

        :return: The name of this CreatePolicyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePolicyResponse.

        策略名

        :param name: The name of this CreatePolicyResponse.
        :type name: str
        """
        self._name = name

    @property
    def package_id(self):
        """Gets the package_id of this CreatePolicyResponse.

        防护包id

        :return: The package_id of this CreatePolicyResponse.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this CreatePolicyResponse.

        防护包id

        :param package_id: The package_id of this CreatePolicyResponse.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def description(self):
        """Gets the description of this CreatePolicyResponse.

        描述

        :return: The description of this CreatePolicyResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePolicyResponse.

        描述

        :param description: The description of this CreatePolicyResponse.
        :type description: str
        """
        self._description = description

    @property
    def clean_threshold(self):
        """Gets the clean_threshold of this CreatePolicyResponse.

        清洗阈值

        :return: The clean_threshold of this CreatePolicyResponse.
        :rtype: int
        """
        return self._clean_threshold

    @clean_threshold.setter
    def clean_threshold(self, clean_threshold):
        """Sets the clean_threshold of this CreatePolicyResponse.

        清洗阈值

        :param clean_threshold: The clean_threshold of this CreatePolicyResponse.
        :type clean_threshold: int
        """
        self._clean_threshold = clean_threshold

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
        if not isinstance(other, CreatePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
