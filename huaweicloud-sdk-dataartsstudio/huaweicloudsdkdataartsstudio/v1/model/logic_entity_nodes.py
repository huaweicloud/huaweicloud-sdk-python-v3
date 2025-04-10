# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicEntityNodes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logic_entity_guid': 'str',
        'logic_entity_name': 'str'
    }

    attribute_map = {
        'logic_entity_guid': 'logic_entity_guid',
        'logic_entity_name': 'logic_entity_name'
    }

    def __init__(self, logic_entity_guid=None, logic_entity_name=None):
        r"""LogicEntityNodes

        The model defined in huaweicloud sdk

        :param logic_entity_guid: 业务资产guid
        :type logic_entity_guid: str
        :param logic_entity_name: 业务资产名称
        :type logic_entity_name: str
        """
        
        

        self._logic_entity_guid = None
        self._logic_entity_name = None
        self.discriminator = None

        if logic_entity_guid is not None:
            self.logic_entity_guid = logic_entity_guid
        if logic_entity_name is not None:
            self.logic_entity_name = logic_entity_name

    @property
    def logic_entity_guid(self):
        r"""Gets the logic_entity_guid of this LogicEntityNodes.

        业务资产guid

        :return: The logic_entity_guid of this LogicEntityNodes.
        :rtype: str
        """
        return self._logic_entity_guid

    @logic_entity_guid.setter
    def logic_entity_guid(self, logic_entity_guid):
        r"""Sets the logic_entity_guid of this LogicEntityNodes.

        业务资产guid

        :param logic_entity_guid: The logic_entity_guid of this LogicEntityNodes.
        :type logic_entity_guid: str
        """
        self._logic_entity_guid = logic_entity_guid

    @property
    def logic_entity_name(self):
        r"""Gets the logic_entity_name of this LogicEntityNodes.

        业务资产名称

        :return: The logic_entity_name of this LogicEntityNodes.
        :rtype: str
        """
        return self._logic_entity_name

    @logic_entity_name.setter
    def logic_entity_name(self, logic_entity_name):
        r"""Sets the logic_entity_name of this LogicEntityNodes.

        业务资产名称

        :param logic_entity_name: The logic_entity_name of this LogicEntityNodes.
        :type logic_entity_name: str
        """
        self._logic_entity_name = logic_entity_name

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
        if not isinstance(other, LogicEntityNodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
