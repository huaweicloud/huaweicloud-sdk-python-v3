# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiAuthVisitParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'api_id': 'str',
        'app_id': 'str',
        'visit_param': 'str'
    }

    attribute_map = {
        'api_id': 'api_id',
        'app_id': 'app_id',
        'visit_param': 'visit_param'
    }

    def __init__(self, api_id=None, app_id=None, visit_param=None):
        """ApiAuthVisitParam

        The model defined in huaweicloud sdk

        :param api_id: 需要授权的API编号
        :type api_id: str
        :param app_id: 需要授权的APP编号
        :type app_id: str
        :param visit_param: 访问参数  支持英文、数字、下划线和中划线，多个参数以英文格式下的逗号隔开，单个参数须以英文或数字结尾且不能重复，且单个参数长度不超过255个字符。
        :type visit_param: str
        """
        
        

        self._api_id = None
        self._app_id = None
        self._visit_param = None
        self.discriminator = None

        self.api_id = api_id
        if app_id is not None:
            self.app_id = app_id
        self.visit_param = visit_param

    @property
    def api_id(self):
        """Gets the api_id of this ApiAuthVisitParam.

        需要授权的API编号

        :return: The api_id of this ApiAuthVisitParam.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ApiAuthVisitParam.

        需要授权的API编号

        :param api_id: The api_id of this ApiAuthVisitParam.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def app_id(self):
        """Gets the app_id of this ApiAuthVisitParam.

        需要授权的APP编号

        :return: The app_id of this ApiAuthVisitParam.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ApiAuthVisitParam.

        需要授权的APP编号

        :param app_id: The app_id of this ApiAuthVisitParam.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def visit_param(self):
        """Gets the visit_param of this ApiAuthVisitParam.

        访问参数  支持英文、数字、下划线和中划线，多个参数以英文格式下的逗号隔开，单个参数须以英文或数字结尾且不能重复，且单个参数长度不超过255个字符。

        :return: The visit_param of this ApiAuthVisitParam.
        :rtype: str
        """
        return self._visit_param

    @visit_param.setter
    def visit_param(self, visit_param):
        """Sets the visit_param of this ApiAuthVisitParam.

        访问参数  支持英文、数字、下划线和中划线，多个参数以英文格式下的逗号隔开，单个参数须以英文或数字结尾且不能重复，且单个参数长度不超过255个字符。

        :param visit_param: The visit_param of this ApiAuthVisitParam.
        :type visit_param: str
        """
        self._visit_param = visit_param

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
        if not isinstance(other, ApiAuthVisitParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
