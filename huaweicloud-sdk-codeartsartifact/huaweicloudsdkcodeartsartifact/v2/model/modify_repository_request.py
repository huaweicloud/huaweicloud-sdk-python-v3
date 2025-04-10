# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyRepositoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tab_id': 'str',
        'body': 'IDERepositoryPair'
    }

    attribute_map = {
        'tab_id': 'tab_id',
        'body': 'body'
    }

    def __init__(self, tab_id=None, body=None):
        r"""ModifyRepositoryRequest

        The model defined in huaweicloud sdk

        :param tab_id: tab_id
        :type tab_id: str
        :param body: Body of the ModifyRepositoryRequest
        :type body: :class:`huaweicloudsdkcodeartsartifact.v2.IDERepositoryPair`
        """
        
        

        self._tab_id = None
        self._body = None
        self.discriminator = None

        self.tab_id = tab_id
        if body is not None:
            self.body = body

    @property
    def tab_id(self):
        r"""Gets the tab_id of this ModifyRepositoryRequest.

        tab_id

        :return: The tab_id of this ModifyRepositoryRequest.
        :rtype: str
        """
        return self._tab_id

    @tab_id.setter
    def tab_id(self, tab_id):
        r"""Sets the tab_id of this ModifyRepositoryRequest.

        tab_id

        :param tab_id: The tab_id of this ModifyRepositoryRequest.
        :type tab_id: str
        """
        self._tab_id = tab_id

    @property
    def body(self):
        r"""Gets the body of this ModifyRepositoryRequest.

        :return: The body of this ModifyRepositoryRequest.
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.IDERepositoryPair`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ModifyRepositoryRequest.

        :param body: The body of this ModifyRepositoryRequest.
        :type body: :class:`huaweicloudsdkcodeartsartifact.v2.IDERepositoryPair`
        """
        self._body = body

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
        if not isinstance(other, ModifyRepositoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
