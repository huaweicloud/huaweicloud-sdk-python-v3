# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteCertificatesResp:

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
        'ret_status': 'str',
        'ret_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ret_status': 'ret_status',
        'ret_code': 'ret_code'
    }

    def __init__(self, id=None, ret_status=None, ret_code=None):
        r"""BatchDeleteCertificatesResp

        The model defined in huaweicloud sdk

        :param id: 证书ID。
        :type id: str
        :param ret_status: 对应id的证书删除后的结果，not found表示证书不存在，successful表示删除成功
        :type ret_status: str
        :param ret_code: 错误码，删除失败时返回此字段
        :type ret_code: str
        """
        
        

        self._id = None
        self._ret_status = None
        self._ret_code = None
        self.discriminator = None

        self.id = id
        self.ret_status = ret_status
        if ret_code is not None:
            self.ret_code = ret_code

    @property
    def id(self):
        r"""Gets the id of this BatchDeleteCertificatesResp.

        证书ID。

        :return: The id of this BatchDeleteCertificatesResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchDeleteCertificatesResp.

        证书ID。

        :param id: The id of this BatchDeleteCertificatesResp.
        :type id: str
        """
        self._id = id

    @property
    def ret_status(self):
        r"""Gets the ret_status of this BatchDeleteCertificatesResp.

        对应id的证书删除后的结果，not found表示证书不存在，successful表示删除成功

        :return: The ret_status of this BatchDeleteCertificatesResp.
        :rtype: str
        """
        return self._ret_status

    @ret_status.setter
    def ret_status(self, ret_status):
        r"""Sets the ret_status of this BatchDeleteCertificatesResp.

        对应id的证书删除后的结果，not found表示证书不存在，successful表示删除成功

        :param ret_status: The ret_status of this BatchDeleteCertificatesResp.
        :type ret_status: str
        """
        self._ret_status = ret_status

    @property
    def ret_code(self):
        r"""Gets the ret_code of this BatchDeleteCertificatesResp.

        错误码，删除失败时返回此字段

        :return: The ret_code of this BatchDeleteCertificatesResp.
        :rtype: str
        """
        return self._ret_code

    @ret_code.setter
    def ret_code(self, ret_code):
        r"""Sets the ret_code of this BatchDeleteCertificatesResp.

        错误码，删除失败时返回此字段

        :param ret_code: The ret_code of this BatchDeleteCertificatesResp.
        :type ret_code: str
        """
        self._ret_code = ret_code

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchDeleteCertificatesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
