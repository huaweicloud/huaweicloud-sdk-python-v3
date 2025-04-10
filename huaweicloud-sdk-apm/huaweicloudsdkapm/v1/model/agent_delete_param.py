# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentDeleteParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_list': 'list[int]',
        'region': 'str',
        'business_id': 'int'
    }

    attribute_map = {
        'instance_list': 'instance_list',
        'region': 'region',
        'business_id': 'business_id'
    }

    def __init__(self, instance_list=None, region=None, business_id=None):
        r"""AgentDeleteParam

        The model defined in huaweicloud sdk

        :param instance_list: 实例列表。
        :type instance_list: list[int]
        :param region: region英文名称。
        :type region: str
        :param business_id: 应用id。
        :type business_id: int
        """
        
        

        self._instance_list = None
        self._region = None
        self._business_id = None
        self.discriminator = None

        self.instance_list = instance_list
        self.region = region
        self.business_id = business_id

    @property
    def instance_list(self):
        r"""Gets the instance_list of this AgentDeleteParam.

        实例列表。

        :return: The instance_list of this AgentDeleteParam.
        :rtype: list[int]
        """
        return self._instance_list

    @instance_list.setter
    def instance_list(self, instance_list):
        r"""Sets the instance_list of this AgentDeleteParam.

        实例列表。

        :param instance_list: The instance_list of this AgentDeleteParam.
        :type instance_list: list[int]
        """
        self._instance_list = instance_list

    @property
    def region(self):
        r"""Gets the region of this AgentDeleteParam.

        region英文名称。

        :return: The region of this AgentDeleteParam.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this AgentDeleteParam.

        region英文名称。

        :param region: The region of this AgentDeleteParam.
        :type region: str
        """
        self._region = region

    @property
    def business_id(self):
        r"""Gets the business_id of this AgentDeleteParam.

        应用id。

        :return: The business_id of this AgentDeleteParam.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        r"""Sets the business_id of this AgentDeleteParam.

        应用id。

        :param business_id: The business_id of this AgentDeleteParam.
        :type business_id: int
        """
        self._business_id = business_id

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
        if not isinstance(other, AgentDeleteParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
