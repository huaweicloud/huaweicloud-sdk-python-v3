# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExceedCutNetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'int',
        'quota': 'str',
        'iccid': 'str'
    }

    attribute_map = {
        'action': 'action',
        'quota': 'quota',
        'iccid': 'iccid'
    }

    def __init__(self, action=None, quota=None, iccid=None):
        r"""ExceedCutNetReq

        The model defined in huaweicloud sdk

        :param action: 操作类型(1:设置达量断网域值，2：取消达量断网域值)
        :type action: int
        :param quota: 阈值,只能是0,-1,正整数，-1表示无限制，0表示有上网流量产生就会立即断网，取消达量断网功能时可不传，单位MB
        :type quota: str
        :param iccid: iccid，传入的sim_card_id为0,则根据iccid进行处理
        :type iccid: str
        """
        
        

        self._action = None
        self._quota = None
        self._iccid = None
        self.discriminator = None

        self.action = action
        if quota is not None:
            self.quota = quota
        if iccid is not None:
            self.iccid = iccid

    @property
    def action(self):
        r"""Gets the action of this ExceedCutNetReq.

        操作类型(1:设置达量断网域值，2：取消达量断网域值)

        :return: The action of this ExceedCutNetReq.
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ExceedCutNetReq.

        操作类型(1:设置达量断网域值，2：取消达量断网域值)

        :param action: The action of this ExceedCutNetReq.
        :type action: int
        """
        self._action = action

    @property
    def quota(self):
        r"""Gets the quota of this ExceedCutNetReq.

        阈值,只能是0,-1,正整数，-1表示无限制，0表示有上网流量产生就会立即断网，取消达量断网功能时可不传，单位MB

        :return: The quota of this ExceedCutNetReq.
        :rtype: str
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ExceedCutNetReq.

        阈值,只能是0,-1,正整数，-1表示无限制，0表示有上网流量产生就会立即断网，取消达量断网功能时可不传，单位MB

        :param quota: The quota of this ExceedCutNetReq.
        :type quota: str
        """
        self._quota = quota

    @property
    def iccid(self):
        r"""Gets the iccid of this ExceedCutNetReq.

        iccid，传入的sim_card_id为0,则根据iccid进行处理

        :return: The iccid of this ExceedCutNetReq.
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        r"""Sets the iccid of this ExceedCutNetReq.

        iccid，传入的sim_card_id为0,则根据iccid进行处理

        :param iccid: The iccid of this ExceedCutNetReq.
        :type iccid: str
        """
        self._iccid = iccid

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
        if not isinstance(other, ExceedCutNetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
