# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportBaseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'list[Success]',
        'failure': 'list[Failure]',
        'swagger': 'Swagger'
    }

    attribute_map = {
        'success': 'success',
        'failure': 'failure',
        'swagger': 'swagger'
    }

    def __init__(self, success=None, failure=None, swagger=None):
        """ImportBaseResult

        The model defined in huaweicloud sdk

        :param success: 导入成功信息
        :type success: list[:class:`huaweicloudsdkapig.v2.Success`]
        :param failure: 导入失败信息
        :type failure: list[:class:`huaweicloudsdkapig.v2.Failure`]
        :param swagger: 
        :type swagger: :class:`huaweicloudsdkapig.v2.Swagger`
        """
        
        

        self._success = None
        self._failure = None
        self._swagger = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if failure is not None:
            self.failure = failure
        if swagger is not None:
            self.swagger = swagger

    @property
    def success(self):
        """Gets the success of this ImportBaseResult.

        导入成功信息

        :return: The success of this ImportBaseResult.
        :rtype: list[:class:`huaweicloudsdkapig.v2.Success`]
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ImportBaseResult.

        导入成功信息

        :param success: The success of this ImportBaseResult.
        :type success: list[:class:`huaweicloudsdkapig.v2.Success`]
        """
        self._success = success

    @property
    def failure(self):
        """Gets the failure of this ImportBaseResult.

        导入失败信息

        :return: The failure of this ImportBaseResult.
        :rtype: list[:class:`huaweicloudsdkapig.v2.Failure`]
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """Sets the failure of this ImportBaseResult.

        导入失败信息

        :param failure: The failure of this ImportBaseResult.
        :type failure: list[:class:`huaweicloudsdkapig.v2.Failure`]
        """
        self._failure = failure

    @property
    def swagger(self):
        """Gets the swagger of this ImportBaseResult.

        :return: The swagger of this ImportBaseResult.
        :rtype: :class:`huaweicloudsdkapig.v2.Swagger`
        """
        return self._swagger

    @swagger.setter
    def swagger(self, swagger):
        """Sets the swagger of this ImportBaseResult.

        :param swagger: The swagger of this ImportBaseResult.
        :type swagger: :class:`huaweicloudsdkapig.v2.Swagger`
        """
        self._swagger = swagger

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
        if not isinstance(other, ImportBaseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
