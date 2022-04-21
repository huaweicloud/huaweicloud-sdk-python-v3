# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelArtsContentReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'access_address': 'str',
        'verify_body': 'str',
        'ak': 'str',
        'sk': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'service_name': 'service_name',
        'access_address': 'access_address',
        'verify_body': 'verify_body',
        'ak': 'ak',
        'sk': 'sk',
        'project_id': 'project_id'
    }

    def __init__(self, service_name=None, access_address=None, verify_body=None, ak=None, sk=None, project_id=None):
        """ModelArtsContentReq

        The model defined in huaweicloud sdk

        :param service_name: 服务名称
        :type service_name: str
        :param access_address: 访问地址
        :type access_address: str
        :param verify_body: 校验参数
        :type verify_body: str
        :param ak: 租户的AK
        :type ak: str
        :param sk: 租户的SK
        :type sk: str
        :param project_id: 项目id
        :type project_id: str
        """
        
        

        self._service_name = None
        self._access_address = None
        self._verify_body = None
        self._ak = None
        self._sk = None
        self._project_id = None
        self.discriminator = None

        self.service_name = service_name
        self.access_address = access_address
        self.verify_body = verify_body
        self.ak = ak
        self.sk = sk
        self.project_id = project_id

    @property
    def service_name(self):
        """Gets the service_name of this ModelArtsContentReq.

        服务名称

        :return: The service_name of this ModelArtsContentReq.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this ModelArtsContentReq.

        服务名称

        :param service_name: The service_name of this ModelArtsContentReq.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def access_address(self):
        """Gets the access_address of this ModelArtsContentReq.

        访问地址

        :return: The access_address of this ModelArtsContentReq.
        :rtype: str
        """
        return self._access_address

    @access_address.setter
    def access_address(self, access_address):
        """Sets the access_address of this ModelArtsContentReq.

        访问地址

        :param access_address: The access_address of this ModelArtsContentReq.
        :type access_address: str
        """
        self._access_address = access_address

    @property
    def verify_body(self):
        """Gets the verify_body of this ModelArtsContentReq.

        校验参数

        :return: The verify_body of this ModelArtsContentReq.
        :rtype: str
        """
        return self._verify_body

    @verify_body.setter
    def verify_body(self, verify_body):
        """Sets the verify_body of this ModelArtsContentReq.

        校验参数

        :param verify_body: The verify_body of this ModelArtsContentReq.
        :type verify_body: str
        """
        self._verify_body = verify_body

    @property
    def ak(self):
        """Gets the ak of this ModelArtsContentReq.

        租户的AK

        :return: The ak of this ModelArtsContentReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this ModelArtsContentReq.

        租户的AK

        :param ak: The ak of this ModelArtsContentReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this ModelArtsContentReq.

        租户的SK

        :return: The sk of this ModelArtsContentReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this ModelArtsContentReq.

        租户的SK

        :param sk: The sk of this ModelArtsContentReq.
        :type sk: str
        """
        self._sk = sk

    @property
    def project_id(self):
        """Gets the project_id of this ModelArtsContentReq.

        项目id

        :return: The project_id of this ModelArtsContentReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ModelArtsContentReq.

        项目id

        :param project_id: The project_id of this ModelArtsContentReq.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ModelArtsContentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
