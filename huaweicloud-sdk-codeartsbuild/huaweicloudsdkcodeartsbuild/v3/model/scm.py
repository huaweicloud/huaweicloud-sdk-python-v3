# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Scm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_tag': 'str',
        'build_commit_id': 'str'
    }

    attribute_map = {
        'build_tag': 'build_tag',
        'build_commit_id': 'build_commit_id'
    }

    def __init__(self, build_tag=None, build_commit_id=None):
        r"""Scm

        The model defined in huaweicloud sdk

        :param build_tag: 代码Tag
        :type build_tag: str
        :param build_commit_id: 代码提交ID
        :type build_commit_id: str
        """
        
        

        self._build_tag = None
        self._build_commit_id = None
        self.discriminator = None

        if build_tag is not None:
            self.build_tag = build_tag
        if build_commit_id is not None:
            self.build_commit_id = build_commit_id

    @property
    def build_tag(self):
        r"""Gets the build_tag of this Scm.

        代码Tag

        :return: The build_tag of this Scm.
        :rtype: str
        """
        return self._build_tag

    @build_tag.setter
    def build_tag(self, build_tag):
        r"""Sets the build_tag of this Scm.

        代码Tag

        :param build_tag: The build_tag of this Scm.
        :type build_tag: str
        """
        self._build_tag = build_tag

    @property
    def build_commit_id(self):
        r"""Gets the build_commit_id of this Scm.

        代码提交ID

        :return: The build_commit_id of this Scm.
        :rtype: str
        """
        return self._build_commit_id

    @build_commit_id.setter
    def build_commit_id(self, build_commit_id):
        r"""Sets the build_commit_id of this Scm.

        代码提交ID

        :param build_commit_id: The build_commit_id of this Scm.
        :type build_commit_id: str
        """
        self._build_commit_id = build_commit_id

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
        if not isinstance(other, Scm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
