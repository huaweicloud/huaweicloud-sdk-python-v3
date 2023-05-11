# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmCreateClusterReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster': 'CdmCreateClusterReqCluster',
        'auto_remind': 'bool',
        'phone_num': 'str',
        'email': 'str'
    }

    attribute_map = {
        'cluster': 'cluster',
        'auto_remind': 'auto_remind',
        'phone_num': 'phone_num',
        'email': 'email'
    }

    def __init__(self, cluster=None, auto_remind=None, phone_num=None, email=None):
        """CdmCreateClusterReq

        The model defined in huaweicloud sdk

        :param cluster: 
        :type cluster: :class:`huaweicloudsdkcdm.v1.CdmCreateClusterReqCluster`
        :param auto_remind: 选择是否开启消息通知。开启后，支持配置5个手机号码或邮箱，作业（目前仅支持表/文件迁移的作业）失败时、EIP异常时会发送短信或邮件通知用户
        :type auto_remind: bool
        :param phone_num: 接收消息通知的手机号码
        :type phone_num: str
        :param email: 接收消息通知的邮箱
        :type email: str
        """
        
        

        self._cluster = None
        self._auto_remind = None
        self._phone_num = None
        self._email = None
        self.discriminator = None

        self.cluster = cluster
        if auto_remind is not None:
            self.auto_remind = auto_remind
        if phone_num is not None:
            self.phone_num = phone_num
        if email is not None:
            self.email = email

    @property
    def cluster(self):
        """Gets the cluster of this CdmCreateClusterReq.

        :return: The cluster of this CdmCreateClusterReq.
        :rtype: :class:`huaweicloudsdkcdm.v1.CdmCreateClusterReqCluster`
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this CdmCreateClusterReq.

        :param cluster: The cluster of this CdmCreateClusterReq.
        :type cluster: :class:`huaweicloudsdkcdm.v1.CdmCreateClusterReqCluster`
        """
        self._cluster = cluster

    @property
    def auto_remind(self):
        """Gets the auto_remind of this CdmCreateClusterReq.

        选择是否开启消息通知。开启后，支持配置5个手机号码或邮箱，作业（目前仅支持表/文件迁移的作业）失败时、EIP异常时会发送短信或邮件通知用户

        :return: The auto_remind of this CdmCreateClusterReq.
        :rtype: bool
        """
        return self._auto_remind

    @auto_remind.setter
    def auto_remind(self, auto_remind):
        """Sets the auto_remind of this CdmCreateClusterReq.

        选择是否开启消息通知。开启后，支持配置5个手机号码或邮箱，作业（目前仅支持表/文件迁移的作业）失败时、EIP异常时会发送短信或邮件通知用户

        :param auto_remind: The auto_remind of this CdmCreateClusterReq.
        :type auto_remind: bool
        """
        self._auto_remind = auto_remind

    @property
    def phone_num(self):
        """Gets the phone_num of this CdmCreateClusterReq.

        接收消息通知的手机号码

        :return: The phone_num of this CdmCreateClusterReq.
        :rtype: str
        """
        return self._phone_num

    @phone_num.setter
    def phone_num(self, phone_num):
        """Sets the phone_num of this CdmCreateClusterReq.

        接收消息通知的手机号码

        :param phone_num: The phone_num of this CdmCreateClusterReq.
        :type phone_num: str
        """
        self._phone_num = phone_num

    @property
    def email(self):
        """Gets the email of this CdmCreateClusterReq.

        接收消息通知的邮箱

        :return: The email of this CdmCreateClusterReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CdmCreateClusterReq.

        接收消息通知的邮箱

        :param email: The email of this CdmCreateClusterReq.
        :type email: str
        """
        self._email = email

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
        if not isinstance(other, CdmCreateClusterReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
