# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchOperateJobRsp:

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
        'status': 'BatchOperateJobStatus',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, id=None, status=None, message=None):
        """BatchOperateJobRsp

        The model defined in huaweicloud sdk

        :param id: 作业id
        :type id: str
        :param status: 
        :type status: :class:`huaweicloudsdkeihealth.v1.BatchOperateJobStatus`
        :param message: 操作结果失败信息，仅在操作失败时会返回
        :type message: str
        """
        
        

        self._id = None
        self._status = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def id(self):
        """Gets the id of this BatchOperateJobRsp.

        作业id

        :return: The id of this BatchOperateJobRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchOperateJobRsp.

        作业id

        :param id: The id of this BatchOperateJobRsp.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this BatchOperateJobRsp.

        :return: The status of this BatchOperateJobRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchOperateJobStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchOperateJobRsp.

        :param status: The status of this BatchOperateJobRsp.
        :type status: :class:`huaweicloudsdkeihealth.v1.BatchOperateJobStatus`
        """
        self._status = status

    @property
    def message(self):
        """Gets the message of this BatchOperateJobRsp.

        操作结果失败信息，仅在操作失败时会返回

        :return: The message of this BatchOperateJobRsp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BatchOperateJobRsp.

        操作结果失败信息，仅在操作失败时会返回

        :param message: The message of this BatchOperateJobRsp.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, BatchOperateJobRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
