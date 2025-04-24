# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeliverTarget:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deliver_target_id': 'str',
        'deliver_target_name': 'str',
        'deliver_status': 'str',
        'deliver_detail_list': 'list[DeliverDetail]'
    }

    attribute_map = {
        'deliver_target_id': 'deliverTargetId',
        'deliver_target_name': 'deliverTargetName',
        'deliver_status': 'deliverStatus',
        'deliver_detail_list': 'deliverDetailList'
    }

    def __init__(self, deliver_target_id=None, deliver_target_name=None, deliver_status=None, deliver_detail_list=None):
        r"""DeliverTarget

        The model defined in huaweicloud sdk

        :param deliver_target_id: 投递目标ID，即事件目标ID
        :type deliver_target_id: str
        :param deliver_target_name: 投递目标名称，及事件目标名称
        :type deliver_target_name: str
        :param deliver_status: 投递状态         SUCCESS Or  FAILED
        :type deliver_status: str
        :param deliver_detail_list: 考虑展示的个数    例如限制只展示最新三条
        :type deliver_detail_list: list[:class:`huaweicloudsdkeg.v1.DeliverDetail`]
        """
        
        

        self._deliver_target_id = None
        self._deliver_target_name = None
        self._deliver_status = None
        self._deliver_detail_list = None
        self.discriminator = None

        if deliver_target_id is not None:
            self.deliver_target_id = deliver_target_id
        if deliver_target_name is not None:
            self.deliver_target_name = deliver_target_name
        if deliver_status is not None:
            self.deliver_status = deliver_status
        if deliver_detail_list is not None:
            self.deliver_detail_list = deliver_detail_list

    @property
    def deliver_target_id(self):
        r"""Gets the deliver_target_id of this DeliverTarget.

        投递目标ID，即事件目标ID

        :return: The deliver_target_id of this DeliverTarget.
        :rtype: str
        """
        return self._deliver_target_id

    @deliver_target_id.setter
    def deliver_target_id(self, deliver_target_id):
        r"""Sets the deliver_target_id of this DeliverTarget.

        投递目标ID，即事件目标ID

        :param deliver_target_id: The deliver_target_id of this DeliverTarget.
        :type deliver_target_id: str
        """
        self._deliver_target_id = deliver_target_id

    @property
    def deliver_target_name(self):
        r"""Gets the deliver_target_name of this DeliverTarget.

        投递目标名称，及事件目标名称

        :return: The deliver_target_name of this DeliverTarget.
        :rtype: str
        """
        return self._deliver_target_name

    @deliver_target_name.setter
    def deliver_target_name(self, deliver_target_name):
        r"""Sets the deliver_target_name of this DeliverTarget.

        投递目标名称，及事件目标名称

        :param deliver_target_name: The deliver_target_name of this DeliverTarget.
        :type deliver_target_name: str
        """
        self._deliver_target_name = deliver_target_name

    @property
    def deliver_status(self):
        r"""Gets the deliver_status of this DeliverTarget.

        投递状态         SUCCESS Or  FAILED

        :return: The deliver_status of this DeliverTarget.
        :rtype: str
        """
        return self._deliver_status

    @deliver_status.setter
    def deliver_status(self, deliver_status):
        r"""Sets the deliver_status of this DeliverTarget.

        投递状态         SUCCESS Or  FAILED

        :param deliver_status: The deliver_status of this DeliverTarget.
        :type deliver_status: str
        """
        self._deliver_status = deliver_status

    @property
    def deliver_detail_list(self):
        r"""Gets the deliver_detail_list of this DeliverTarget.

        考虑展示的个数    例如限制只展示最新三条

        :return: The deliver_detail_list of this DeliverTarget.
        :rtype: list[:class:`huaweicloudsdkeg.v1.DeliverDetail`]
        """
        return self._deliver_detail_list

    @deliver_detail_list.setter
    def deliver_detail_list(self, deliver_detail_list):
        r"""Sets the deliver_detail_list of this DeliverTarget.

        考虑展示的个数    例如限制只展示最新三条

        :param deliver_detail_list: The deliver_detail_list of this DeliverTarget.
        :type deliver_detail_list: list[:class:`huaweicloudsdkeg.v1.DeliverDetail`]
        """
        self._deliver_detail_list = deliver_detail_list

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
        if not isinstance(other, DeliverTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
