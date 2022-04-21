# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FunctionGraphContentReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'function_name': 'str',
        'orig_url': 'str',
        'final_url': 'str',
        'verify_body': 'str',
        'ak': 'str',
        'sk': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'function_name': 'function_name',
        'orig_url': 'orig_url',
        'final_url': 'final_url',
        'verify_body': 'verify_body',
        'ak': 'ak',
        'sk': 'sk',
        'project_id': 'project_id'
    }

    def __init__(self, function_name=None, orig_url=None, final_url=None, verify_body=None, ak=None, sk=None, project_id=None):
        """FunctionGraphContentReq

        The model defined in huaweicloud sdk

        :param function_name: 名称
        :type function_name: str
        :param orig_url: 原始URL
        :type orig_url: str
        :param final_url: 转换后的URL
        :type final_url: str
        :param verify_body: 校验参数
        :type verify_body: str
        :param ak: 租户的AK
        :type ak: str
        :param sk: 租户的SK
        :type sk: str
        :param project_id: 项目id
        :type project_id: str
        """
        
        

        self._function_name = None
        self._orig_url = None
        self._final_url = None
        self._verify_body = None
        self._ak = None
        self._sk = None
        self._project_id = None
        self.discriminator = None

        self.function_name = function_name
        self.orig_url = orig_url
        self.final_url = final_url
        self.verify_body = verify_body
        self.ak = ak
        self.sk = sk
        self.project_id = project_id

    @property
    def function_name(self):
        """Gets the function_name of this FunctionGraphContentReq.

        名称

        :return: The function_name of this FunctionGraphContentReq.
        :rtype: str
        """
        return self._function_name

    @function_name.setter
    def function_name(self, function_name):
        """Sets the function_name of this FunctionGraphContentReq.

        名称

        :param function_name: The function_name of this FunctionGraphContentReq.
        :type function_name: str
        """
        self._function_name = function_name

    @property
    def orig_url(self):
        """Gets the orig_url of this FunctionGraphContentReq.

        原始URL

        :return: The orig_url of this FunctionGraphContentReq.
        :rtype: str
        """
        return self._orig_url

    @orig_url.setter
    def orig_url(self, orig_url):
        """Sets the orig_url of this FunctionGraphContentReq.

        原始URL

        :param orig_url: The orig_url of this FunctionGraphContentReq.
        :type orig_url: str
        """
        self._orig_url = orig_url

    @property
    def final_url(self):
        """Gets the final_url of this FunctionGraphContentReq.

        转换后的URL

        :return: The final_url of this FunctionGraphContentReq.
        :rtype: str
        """
        return self._final_url

    @final_url.setter
    def final_url(self, final_url):
        """Sets the final_url of this FunctionGraphContentReq.

        转换后的URL

        :param final_url: The final_url of this FunctionGraphContentReq.
        :type final_url: str
        """
        self._final_url = final_url

    @property
    def verify_body(self):
        """Gets the verify_body of this FunctionGraphContentReq.

        校验参数

        :return: The verify_body of this FunctionGraphContentReq.
        :rtype: str
        """
        return self._verify_body

    @verify_body.setter
    def verify_body(self, verify_body):
        """Sets the verify_body of this FunctionGraphContentReq.

        校验参数

        :param verify_body: The verify_body of this FunctionGraphContentReq.
        :type verify_body: str
        """
        self._verify_body = verify_body

    @property
    def ak(self):
        """Gets the ak of this FunctionGraphContentReq.

        租户的AK

        :return: The ak of this FunctionGraphContentReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this FunctionGraphContentReq.

        租户的AK

        :param ak: The ak of this FunctionGraphContentReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this FunctionGraphContentReq.

        租户的SK

        :return: The sk of this FunctionGraphContentReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this FunctionGraphContentReq.

        租户的SK

        :param sk: The sk of this FunctionGraphContentReq.
        :type sk: str
        """
        self._sk = sk

    @property
    def project_id(self):
        """Gets the project_id of this FunctionGraphContentReq.

        项目id

        :return: The project_id of this FunctionGraphContentReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this FunctionGraphContentReq.

        项目id

        :param project_id: The project_id of this FunctionGraphContentReq.
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
        if not isinstance(other, FunctionGraphContentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
