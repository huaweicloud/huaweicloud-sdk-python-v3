# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemSimpleDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'related_id': 'str',
        'related_url': 'str'
    }

    attribute_map = {
        'related_id': 'related_id',
        'related_url': 'related_url'
    }

    def __init__(self, related_id=None, related_url=None):
        r"""WorkItemSimpleDto

        The model defined in huaweicloud sdk

        :param related_id: **参数解释：** 工作项编号。
        :type related_id: str
        :param related_url: **参数解释：** 工作项地址。
        :type related_url: str
        """
        
        

        self._related_id = None
        self._related_url = None
        self.discriminator = None

        if related_id is not None:
            self.related_id = related_id
        if related_url is not None:
            self.related_url = related_url

    @property
    def related_id(self):
        r"""Gets the related_id of this WorkItemSimpleDto.

        **参数解释：** 工作项编号。

        :return: The related_id of this WorkItemSimpleDto.
        :rtype: str
        """
        return self._related_id

    @related_id.setter
    def related_id(self, related_id):
        r"""Sets the related_id of this WorkItemSimpleDto.

        **参数解释：** 工作项编号。

        :param related_id: The related_id of this WorkItemSimpleDto.
        :type related_id: str
        """
        self._related_id = related_id

    @property
    def related_url(self):
        r"""Gets the related_url of this WorkItemSimpleDto.

        **参数解释：** 工作项地址。

        :return: The related_url of this WorkItemSimpleDto.
        :rtype: str
        """
        return self._related_url

    @related_url.setter
    def related_url(self, related_url):
        r"""Sets the related_url of this WorkItemSimpleDto.

        **参数解释：** 工作项地址。

        :param related_url: The related_url of this WorkItemSimpleDto.
        :type related_url: str
        """
        self._related_url = related_url

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
        if not isinstance(other, WorkItemSimpleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
