# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionExtends:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_ids': 'Tag',
        'domain_ids': 'list[str]',
        'source': 'str'
    }

    attribute_map = {
        'tag_ids': 'tag_ids',
        'domain_ids': 'domain_ids',
        'source': 'source'
    }

    def __init__(self, tag_ids=None, domain_ids=None, source=None):
        """SessionExtends

        The model defined in huaweicloud sdk

        :param tag_ids: 
        :type tag_ids: :class:`huaweicloudsdkcbs.v1.Tag`
        :param domain_ids: 领域列表，多个领域用分号隔开。如果设置了领域且领域不为空，就从这些领域中匹配答案，否则就从该用户的全部知识库匹配答案。  当前最多支持10个领域。 
        :type domain_ids: list[str]
        :param source: 问题来源 其他支持用户自定义，最终体现在问答日志里
        :type source: str
        """
        
        

        self._tag_ids = None
        self._domain_ids = None
        self._source = None
        self.discriminator = None

        if tag_ids is not None:
            self.tag_ids = tag_ids
        if domain_ids is not None:
            self.domain_ids = domain_ids
        if source is not None:
            self.source = source

    @property
    def tag_ids(self):
        """Gets the tag_ids of this SessionExtends.

        :return: The tag_ids of this SessionExtends.
        :rtype: :class:`huaweicloudsdkcbs.v1.Tag`
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this SessionExtends.

        :param tag_ids: The tag_ids of this SessionExtends.
        :type tag_ids: :class:`huaweicloudsdkcbs.v1.Tag`
        """
        self._tag_ids = tag_ids

    @property
    def domain_ids(self):
        """Gets the domain_ids of this SessionExtends.

        领域列表，多个领域用分号隔开。如果设置了领域且领域不为空，就从这些领域中匹配答案，否则就从该用户的全部知识库匹配答案。  当前最多支持10个领域。 

        :return: The domain_ids of this SessionExtends.
        :rtype: list[str]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        """Sets the domain_ids of this SessionExtends.

        领域列表，多个领域用分号隔开。如果设置了领域且领域不为空，就从这些领域中匹配答案，否则就从该用户的全部知识库匹配答案。  当前最多支持10个领域。 

        :param domain_ids: The domain_ids of this SessionExtends.
        :type domain_ids: list[str]
        """
        self._domain_ids = domain_ids

    @property
    def source(self):
        """Gets the source of this SessionExtends.

        问题来源 其他支持用户自定义，最终体现在问答日志里

        :return: The source of this SessionExtends.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SessionExtends.

        问题来源 其他支持用户自定义，最终体现在问答日志里

        :param source: The source of this SessionExtends.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, SessionExtends):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
