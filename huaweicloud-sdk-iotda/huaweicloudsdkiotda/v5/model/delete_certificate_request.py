# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCertificateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('sp_auth_token')
    sensitive_list.append('stage_auth_token')

    openapi_types = {
        'sp_auth_token': 'str',
        'stage_auth_token': 'str',
        'instance_id': 'str',
        'certificate_id': 'str'
    }

    attribute_map = {
        'sp_auth_token': 'Sp-Auth-Token',
        'stage_auth_token': 'Stage-Auth-Token',
        'instance_id': 'Instance-Id',
        'certificate_id': 'certificate_id'
    }

    def __init__(self, sp_auth_token=None, stage_auth_token=None, instance_id=None, certificate_id=None):
        """DeleteCertificateRequest

        The model defined in huaweicloud sdk

        :param sp_auth_token: Sp用户Token。通过调用IoBPS服务获取SP用户Token
        :type sp_auth_token: str
        :param stage_auth_token: Stage用户的Token, 仅提供给IoStage服务使用
        :type stage_auth_token: str
        :param instance_id: 实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。
        :type instance_id: str
        :param certificate_id: 设备CA证书ID，在上传设备CA证书时由平台分配的唯一标识。
        :type certificate_id: str
        """
        
        

        self._sp_auth_token = None
        self._stage_auth_token = None
        self._instance_id = None
        self._certificate_id = None
        self.discriminator = None

        if sp_auth_token is not None:
            self.sp_auth_token = sp_auth_token
        if stage_auth_token is not None:
            self.stage_auth_token = stage_auth_token
        if instance_id is not None:
            self.instance_id = instance_id
        self.certificate_id = certificate_id

    @property
    def sp_auth_token(self):
        """Gets the sp_auth_token of this DeleteCertificateRequest.

        Sp用户Token。通过调用IoBPS服务获取SP用户Token

        :return: The sp_auth_token of this DeleteCertificateRequest.
        :rtype: str
        """
        return self._sp_auth_token

    @sp_auth_token.setter
    def sp_auth_token(self, sp_auth_token):
        """Sets the sp_auth_token of this DeleteCertificateRequest.

        Sp用户Token。通过调用IoBPS服务获取SP用户Token

        :param sp_auth_token: The sp_auth_token of this DeleteCertificateRequest.
        :type sp_auth_token: str
        """
        self._sp_auth_token = sp_auth_token

    @property
    def stage_auth_token(self):
        """Gets the stage_auth_token of this DeleteCertificateRequest.

        Stage用户的Token, 仅提供给IoStage服务使用

        :return: The stage_auth_token of this DeleteCertificateRequest.
        :rtype: str
        """
        return self._stage_auth_token

    @stage_auth_token.setter
    def stage_auth_token(self, stage_auth_token):
        """Sets the stage_auth_token of this DeleteCertificateRequest.

        Stage用户的Token, 仅提供给IoStage服务使用

        :param stage_auth_token: The stage_auth_token of this DeleteCertificateRequest.
        :type stage_auth_token: str
        """
        self._stage_auth_token = stage_auth_token

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteCertificateRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this DeleteCertificateRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteCertificateRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this DeleteCertificateRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this DeleteCertificateRequest.

        设备CA证书ID，在上传设备CA证书时由平台分配的唯一标识。

        :return: The certificate_id of this DeleteCertificateRequest.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this DeleteCertificateRequest.

        设备CA证书ID，在上传设备CA证书时由平台分配的唯一标识。

        :param certificate_id: The certificate_id of this DeleteCertificateRequest.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

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
        if not isinstance(other, DeleteCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
