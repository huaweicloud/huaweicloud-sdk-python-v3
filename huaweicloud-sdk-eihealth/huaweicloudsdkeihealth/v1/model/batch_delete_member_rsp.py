# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteMemberRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, id=None, name=None, status=None, failed_reason=None):
        r"""BatchDeleteMemberRsp

        The model defined in huaweicloud sdk

        :param id: 用户id
        :type id: str
        :param name: 用户名
        :type name: str
        :param status: 删除结果
        :type status: str
        :param failed_reason: 失败原因
        :type failed_reason: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._failed_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def id(self):
        r"""Gets the id of this BatchDeleteMemberRsp.

        用户id

        :return: The id of this BatchDeleteMemberRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchDeleteMemberRsp.

        用户id

        :param id: The id of this BatchDeleteMemberRsp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BatchDeleteMemberRsp.

        用户名

        :return: The name of this BatchDeleteMemberRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchDeleteMemberRsp.

        用户名

        :param name: The name of this BatchDeleteMemberRsp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this BatchDeleteMemberRsp.

        删除结果

        :return: The status of this BatchDeleteMemberRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchDeleteMemberRsp.

        删除结果

        :param status: The status of this BatchDeleteMemberRsp.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this BatchDeleteMemberRsp.

        失败原因

        :return: The failed_reason of this BatchDeleteMemberRsp.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this BatchDeleteMemberRsp.

        失败原因

        :param failed_reason: The failed_reason of this BatchDeleteMemberRsp.
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
        if not isinstance(other, BatchDeleteMemberRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
