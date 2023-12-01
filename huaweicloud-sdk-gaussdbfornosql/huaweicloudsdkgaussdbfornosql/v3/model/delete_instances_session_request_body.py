# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteInstancesSessionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_all': 'bool',
        'session_ids': 'list[str]'
    }

    attribute_map = {
        'is_all': 'is_all',
        'session_ids': 'session_ids'
    }

    def __init__(self, is_all=None, session_ids=None):
        """DeleteInstancesSessionRequestBody

        The model defined in huaweicloud sdk

        :param is_all: 是否删除全部会话。
        :type is_all: bool
        :param session_ids: 需要删除的会话id。is_all为false的时候，session_ids为必填，不能为空。
        :type session_ids: list[str]
        """
        
        

        self._is_all = None
        self._session_ids = None
        self.discriminator = None

        self.is_all = is_all
        if session_ids is not None:
            self.session_ids = session_ids

    @property
    def is_all(self):
        """Gets the is_all of this DeleteInstancesSessionRequestBody.

        是否删除全部会话。

        :return: The is_all of this DeleteInstancesSessionRequestBody.
        :rtype: bool
        """
        return self._is_all

    @is_all.setter
    def is_all(self, is_all):
        """Sets the is_all of this DeleteInstancesSessionRequestBody.

        是否删除全部会话。

        :param is_all: The is_all of this DeleteInstancesSessionRequestBody.
        :type is_all: bool
        """
        self._is_all = is_all

    @property
    def session_ids(self):
        """Gets the session_ids of this DeleteInstancesSessionRequestBody.

        需要删除的会话id。is_all为false的时候，session_ids为必填，不能为空。

        :return: The session_ids of this DeleteInstancesSessionRequestBody.
        :rtype: list[str]
        """
        return self._session_ids

    @session_ids.setter
    def session_ids(self, session_ids):
        """Sets the session_ids of this DeleteInstancesSessionRequestBody.

        需要删除的会话id。is_all为false的时候，session_ids为必填，不能为空。

        :param session_ids: The session_ids of this DeleteInstancesSessionRequestBody.
        :type session_ids: list[str]
        """
        self._session_ids = session_ids

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
        if not isinstance(other, DeleteInstancesSessionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
