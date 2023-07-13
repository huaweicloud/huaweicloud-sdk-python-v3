# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeliverDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deliver_time': 'str',
        'deliver_status': 'str',
        'deliver_consuming': 'str',
        'deliver_rsp_code': 'str'
    }

    attribute_map = {
        'deliver_time': 'deliverTime',
        'deliver_status': 'deliverStatus',
        'deliver_consuming': 'deliverConsuming',
        'deliver_rsp_code': 'deliverRspCode'
    }

    def __init__(self, deliver_time=None, deliver_status=None, deliver_consuming=None, deliver_rsp_code=None):
        """DeliverDetail

        The model defined in huaweicloud sdk

        :param deliver_time: 投递时间   格式 yyyy/mm/dd xx:yy:zz
        :type deliver_time: str
        :param deliver_status: 投递状态     SUCCESS Or  FAILED
        :type deliver_status: str
        :param deliver_consuming: 投递耗时，单位ms
        :type deliver_consuming: str
        :param deliver_rsp_code: 投递响应码
        :type deliver_rsp_code: str
        """
        
        

        self._deliver_time = None
        self._deliver_status = None
        self._deliver_consuming = None
        self._deliver_rsp_code = None
        self.discriminator = None

        if deliver_time is not None:
            self.deliver_time = deliver_time
        if deliver_status is not None:
            self.deliver_status = deliver_status
        if deliver_consuming is not None:
            self.deliver_consuming = deliver_consuming
        if deliver_rsp_code is not None:
            self.deliver_rsp_code = deliver_rsp_code

    @property
    def deliver_time(self):
        """Gets the deliver_time of this DeliverDetail.

        投递时间   格式 yyyy/mm/dd xx:yy:zz

        :return: The deliver_time of this DeliverDetail.
        :rtype: str
        """
        return self._deliver_time

    @deliver_time.setter
    def deliver_time(self, deliver_time):
        """Sets the deliver_time of this DeliverDetail.

        投递时间   格式 yyyy/mm/dd xx:yy:zz

        :param deliver_time: The deliver_time of this DeliverDetail.
        :type deliver_time: str
        """
        self._deliver_time = deliver_time

    @property
    def deliver_status(self):
        """Gets the deliver_status of this DeliverDetail.

        投递状态     SUCCESS Or  FAILED

        :return: The deliver_status of this DeliverDetail.
        :rtype: str
        """
        return self._deliver_status

    @deliver_status.setter
    def deliver_status(self, deliver_status):
        """Sets the deliver_status of this DeliverDetail.

        投递状态     SUCCESS Or  FAILED

        :param deliver_status: The deliver_status of this DeliverDetail.
        :type deliver_status: str
        """
        self._deliver_status = deliver_status

    @property
    def deliver_consuming(self):
        """Gets the deliver_consuming of this DeliverDetail.

        投递耗时，单位ms

        :return: The deliver_consuming of this DeliverDetail.
        :rtype: str
        """
        return self._deliver_consuming

    @deliver_consuming.setter
    def deliver_consuming(self, deliver_consuming):
        """Sets the deliver_consuming of this DeliverDetail.

        投递耗时，单位ms

        :param deliver_consuming: The deliver_consuming of this DeliverDetail.
        :type deliver_consuming: str
        """
        self._deliver_consuming = deliver_consuming

    @property
    def deliver_rsp_code(self):
        """Gets the deliver_rsp_code of this DeliverDetail.

        投递响应码

        :return: The deliver_rsp_code of this DeliverDetail.
        :rtype: str
        """
        return self._deliver_rsp_code

    @deliver_rsp_code.setter
    def deliver_rsp_code(self, deliver_rsp_code):
        """Sets the deliver_rsp_code of this DeliverDetail.

        投递响应码

        :param deliver_rsp_code: The deliver_rsp_code of this DeliverDetail.
        :type deliver_rsp_code: str
        """
        self._deliver_rsp_code = deliver_rsp_code

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
        if not isinstance(other, DeliverDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
