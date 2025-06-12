# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobStatusBody:

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
        'abort_status': 'str',
        'label': 'str'
    }

    attribute_map = {
        'status': 'status',
        'abort_status': 'abort_status',
        'label': 'label'
    }

    def __init__(self, status=None, abort_status=None, label=None):
        r"""JobStatusBody

        The model defined in huaweicloud sdk

        :param status: 任务状态
        :type status: str
        :param abort_status: 任务终止状态
        :type abort_status: str
        :param label: 标签
        :type label: str
        """
        
        

        self._status = None
        self._abort_status = None
        self._label = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if abort_status is not None:
            self.abort_status = abort_status
        if label is not None:
            self.label = label

    @property
    def status(self):
        r"""Gets the status of this JobStatusBody.

        任务状态

        :return: The status of this JobStatusBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobStatusBody.

        任务状态

        :param status: The status of this JobStatusBody.
        :type status: str
        """
        self._status = status

    @property
    def abort_status(self):
        r"""Gets the abort_status of this JobStatusBody.

        任务终止状态

        :return: The abort_status of this JobStatusBody.
        :rtype: str
        """
        return self._abort_status

    @abort_status.setter
    def abort_status(self, abort_status):
        r"""Sets the abort_status of this JobStatusBody.

        任务终止状态

        :param abort_status: The abort_status of this JobStatusBody.
        :type abort_status: str
        """
        self._abort_status = abort_status

    @property
    def label(self):
        r"""Gets the label of this JobStatusBody.

        标签

        :return: The label of this JobStatusBody.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this JobStatusBody.

        标签

        :param label: The label of this JobStatusBody.
        :type label: str
        """
        self._label = label

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
        if not isinstance(other, JobStatusBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
