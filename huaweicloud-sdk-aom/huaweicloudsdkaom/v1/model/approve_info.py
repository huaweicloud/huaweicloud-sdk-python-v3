# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApproveInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_selected': 'str',
        'need_approve': 'bool',
        'smn_urn_list': 'str'
    }

    attribute_map = {
        'topic_selected': 'topic_selected',
        'need_approve': 'need_approve',
        'smn_urn_list': 'smn_urn_list'
    }

    def __init__(self, topic_selected=None, need_approve=None, smn_urn_list=None):
        """ApproveInfo

        The model defined in huaweicloud sdk

        :param topic_selected: 审批人主题选择。
        :type topic_selected: str
        :param need_approve: 是否审核,默认是不审核，true，false。
        :type need_approve: bool
        :param smn_urn_list: 审批主题urn集合。
        :type smn_urn_list: str
        """
        
        

        self._topic_selected = None
        self._need_approve = None
        self._smn_urn_list = None
        self.discriminator = None

        if topic_selected is not None:
            self.topic_selected = topic_selected
        if need_approve is not None:
            self.need_approve = need_approve
        if smn_urn_list is not None:
            self.smn_urn_list = smn_urn_list

    @property
    def topic_selected(self):
        """Gets the topic_selected of this ApproveInfo.

        审批人主题选择。

        :return: The topic_selected of this ApproveInfo.
        :rtype: str
        """
        return self._topic_selected

    @topic_selected.setter
    def topic_selected(self, topic_selected):
        """Sets the topic_selected of this ApproveInfo.

        审批人主题选择。

        :param topic_selected: The topic_selected of this ApproveInfo.
        :type topic_selected: str
        """
        self._topic_selected = topic_selected

    @property
    def need_approve(self):
        """Gets the need_approve of this ApproveInfo.

        是否审核,默认是不审核，true，false。

        :return: The need_approve of this ApproveInfo.
        :rtype: bool
        """
        return self._need_approve

    @need_approve.setter
    def need_approve(self, need_approve):
        """Sets the need_approve of this ApproveInfo.

        是否审核,默认是不审核，true，false。

        :param need_approve: The need_approve of this ApproveInfo.
        :type need_approve: bool
        """
        self._need_approve = need_approve

    @property
    def smn_urn_list(self):
        """Gets the smn_urn_list of this ApproveInfo.

        审批主题urn集合。

        :return: The smn_urn_list of this ApproveInfo.
        :rtype: str
        """
        return self._smn_urn_list

    @smn_urn_list.setter
    def smn_urn_list(self, smn_urn_list):
        """Sets the smn_urn_list of this ApproveInfo.

        审批主题urn集合。

        :param smn_urn_list: The smn_urn_list of this ApproveInfo.
        :type smn_urn_list: str
        """
        self._smn_urn_list = smn_urn_list

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
        if not isinstance(other, ApproveInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
