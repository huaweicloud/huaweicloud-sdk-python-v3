# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseRealtionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'case_id': 'str',
        'simple_description': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'case_id': 'case_id',
        'simple_description': 'simple_description',
        'user_name': 'user_name'
    }

    def __init__(self, case_id=None, simple_description=None, user_name=None):
        """CaseRealtionInfo

        The model defined in huaweicloud sdk

        :param case_id: 工单id
        :type case_id: str
        :param simple_description: 简要描述
        :type simple_description: str
        :param user_name: 提交人，即用户名称
        :type user_name: str
        """
        
        

        self._case_id = None
        self._simple_description = None
        self._user_name = None
        self.discriminator = None

        if case_id is not None:
            self.case_id = case_id
        if simple_description is not None:
            self.simple_description = simple_description
        if user_name is not None:
            self.user_name = user_name

    @property
    def case_id(self):
        """Gets the case_id of this CaseRealtionInfo.

        工单id

        :return: The case_id of this CaseRealtionInfo.
        :rtype: str
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        """Sets the case_id of this CaseRealtionInfo.

        工单id

        :param case_id: The case_id of this CaseRealtionInfo.
        :type case_id: str
        """
        self._case_id = case_id

    @property
    def simple_description(self):
        """Gets the simple_description of this CaseRealtionInfo.

        简要描述

        :return: The simple_description of this CaseRealtionInfo.
        :rtype: str
        """
        return self._simple_description

    @simple_description.setter
    def simple_description(self, simple_description):
        """Sets the simple_description of this CaseRealtionInfo.

        简要描述

        :param simple_description: The simple_description of this CaseRealtionInfo.
        :type simple_description: str
        """
        self._simple_description = simple_description

    @property
    def user_name(self):
        """Gets the user_name of this CaseRealtionInfo.

        提交人，即用户名称

        :return: The user_name of this CaseRealtionInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CaseRealtionInfo.

        提交人，即用户名称

        :param user_name: The user_name of this CaseRealtionInfo.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, CaseRealtionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
