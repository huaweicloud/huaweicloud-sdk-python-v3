# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestRenamePartReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'participant_id': 'str',
        'number': 'str',
        'new_name': 'str'
    }

    attribute_map = {
        'participant_id': 'participantID',
        'number': 'number',
        'new_name': 'newName'
    }

    def __init__(self, participant_id=None, number=None, new_name=None):
        """RestRenamePartReqBody

        The model defined in huaweicloud sdk

        :param participant_id: 与会者标识。 已入会的必须填写该字段。
        :type participant_id: str
        :param number: 与会者号码。
        :type number: str
        :param new_name: 新名称。
        :type new_name: str
        """
        
        

        self._participant_id = None
        self._number = None
        self._new_name = None
        self.discriminator = None

        if participant_id is not None:
            self.participant_id = participant_id
        self.number = number
        self.new_name = new_name

    @property
    def participant_id(self):
        """Gets the participant_id of this RestRenamePartReqBody.

        与会者标识。 已入会的必须填写该字段。

        :return: The participant_id of this RestRenamePartReqBody.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this RestRenamePartReqBody.

        与会者标识。 已入会的必须填写该字段。

        :param participant_id: The participant_id of this RestRenamePartReqBody.
        :type participant_id: str
        """
        self._participant_id = participant_id

    @property
    def number(self):
        """Gets the number of this RestRenamePartReqBody.

        与会者号码。

        :return: The number of this RestRenamePartReqBody.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this RestRenamePartReqBody.

        与会者号码。

        :param number: The number of this RestRenamePartReqBody.
        :type number: str
        """
        self._number = number

    @property
    def new_name(self):
        """Gets the new_name of this RestRenamePartReqBody.

        新名称。

        :return: The new_name of this RestRenamePartReqBody.
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this RestRenamePartReqBody.

        新名称。

        :param new_name: The new_name of this RestRenamePartReqBody.
        :type new_name: str
        """
        self._new_name = new_name

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
        if not isinstance(other, RestRenamePartReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
