# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateRepositoryMemberDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'result': 'list[CreateRepositoryMemberResponseDto]'
    }

    attribute_map = {
        'status': 'status',
        'result': 'result'
    }

    def __init__(self, status=None, result=None):
        r"""BatchCreateRepositoryMemberDto

        The model defined in huaweicloud sdk

        :param status: **参数解释：** 批量添加是否成功 **约束限制：** - success，全部添加成功。 - error，未全部添加成功。
        :type status: str
        :param result: **参数解释：** 批量添加结果详情。 **约束限制：** 不涉及。
        :type result: list[:class:`huaweicloudsdkcodehub.v4.CreateRepositoryMemberResponseDto`]
        """
        
        

        self._status = None
        self._result = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if result is not None:
            self.result = result

    @property
    def status(self):
        r"""Gets the status of this BatchCreateRepositoryMemberDto.

        **参数解释：** 批量添加是否成功 **约束限制：** - success，全部添加成功。 - error，未全部添加成功。

        :return: The status of this BatchCreateRepositoryMemberDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchCreateRepositoryMemberDto.

        **参数解释：** 批量添加是否成功 **约束限制：** - success，全部添加成功。 - error，未全部添加成功。

        :param status: The status of this BatchCreateRepositoryMemberDto.
        :type status: str
        """
        self._status = status

    @property
    def result(self):
        r"""Gets the result of this BatchCreateRepositoryMemberDto.

        **参数解释：** 批量添加结果详情。 **约束限制：** 不涉及。

        :return: The result of this BatchCreateRepositoryMemberDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.CreateRepositoryMemberResponseDto`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this BatchCreateRepositoryMemberDto.

        **参数解释：** 批量添加结果详情。 **约束限制：** 不涉及。

        :param result: The result of this BatchCreateRepositoryMemberDto.
        :type result: list[:class:`huaweicloudsdkcodehub.v4.CreateRepositoryMemberResponseDto`]
        """
        self._result = result

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
        if not isinstance(other, BatchCreateRepositoryMemberDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
