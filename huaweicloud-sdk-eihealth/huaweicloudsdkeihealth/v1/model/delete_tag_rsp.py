# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTagRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag': 'str',
        'status': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'status': 'status',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, tag=None, status=None, failed_reason=None):
        """DeleteTagRsp

        The model defined in huaweicloud sdk

        :param tag: 镜像tag名称
        :type tag: str
        :param status: 删除结果
        :type status: str
        :param failed_reason: 失败原因
        :type failed_reason: str
        """
        
        

        self._tag = None
        self._status = None
        self._failed_reason = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def tag(self):
        """Gets the tag of this DeleteTagRsp.

        镜像tag名称

        :return: The tag of this DeleteTagRsp.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this DeleteTagRsp.

        镜像tag名称

        :param tag: The tag of this DeleteTagRsp.
        :type tag: str
        """
        self._tag = tag

    @property
    def status(self):
        """Gets the status of this DeleteTagRsp.

        删除结果

        :return: The status of this DeleteTagRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeleteTagRsp.

        删除结果

        :param status: The status of this DeleteTagRsp.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        """Gets the failed_reason of this DeleteTagRsp.

        失败原因

        :return: The failed_reason of this DeleteTagRsp.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this DeleteTagRsp.

        失败原因

        :param failed_reason: The failed_reason of this DeleteTagRsp.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

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
        if not isinstance(other, DeleteTagRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
