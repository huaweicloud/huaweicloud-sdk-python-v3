# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertKeyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'enable_ca_cert': 'bool'
    }

    attribute_map = {
        'task_id': 'task_id',
        'enable_ca_cert': 'enable_ca_cert'
    }

    def __init__(self, task_id=None, enable_ca_cert=None):
        r"""ShowCertKeyRequest

        The model defined in huaweicloud sdk

        :param task_id: 迁移任务ID
        :type task_id: str
        :param enable_ca_cert: 是否生成ca证书
        :type enable_ca_cert: bool
        """
        
        

        self._task_id = None
        self._enable_ca_cert = None
        self.discriminator = None

        self.task_id = task_id
        if enable_ca_cert is not None:
            self.enable_ca_cert = enable_ca_cert

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowCertKeyRequest.

        迁移任务ID

        :return: The task_id of this ShowCertKeyRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowCertKeyRequest.

        迁移任务ID

        :param task_id: The task_id of this ShowCertKeyRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def enable_ca_cert(self):
        r"""Gets the enable_ca_cert of this ShowCertKeyRequest.

        是否生成ca证书

        :return: The enable_ca_cert of this ShowCertKeyRequest.
        :rtype: bool
        """
        return self._enable_ca_cert

    @enable_ca_cert.setter
    def enable_ca_cert(self, enable_ca_cert):
        r"""Sets the enable_ca_cert of this ShowCertKeyRequest.

        是否生成ca证书

        :param enable_ca_cert: The enable_ca_cert of this ShowCertKeyRequest.
        :type enable_ca_cert: bool
        """
        self._enable_ca_cert = enable_ca_cert

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
        if not isinstance(other, ShowCertKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
