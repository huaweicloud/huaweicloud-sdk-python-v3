# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStarRocksDbParametersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_parameters': 'list[DbParameter]'
    }

    attribute_map = {
        'db_parameters': 'db_parameters'
    }

    def __init__(self, db_parameters=None):
        r"""ListStarRocksDbParametersResponse

        The model defined in huaweicloud sdk

        :param db_parameters: 库参数信息。
        :type db_parameters: list[:class:`huaweicloudsdkgaussdb.v3.DbParameter`]
        """
        
        super(ListStarRocksDbParametersResponse, self).__init__()

        self._db_parameters = None
        self.discriminator = None

        if db_parameters is not None:
            self.db_parameters = db_parameters

    @property
    def db_parameters(self):
        r"""Gets the db_parameters of this ListStarRocksDbParametersResponse.

        库参数信息。

        :return: The db_parameters of this ListStarRocksDbParametersResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.DbParameter`]
        """
        return self._db_parameters

    @db_parameters.setter
    def db_parameters(self, db_parameters):
        r"""Sets the db_parameters of this ListStarRocksDbParametersResponse.

        库参数信息。

        :param db_parameters: The db_parameters of this ListStarRocksDbParametersResponse.
        :type db_parameters: list[:class:`huaweicloudsdkgaussdb.v3.DbParameter`]
        """
        self._db_parameters = db_parameters

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
        if not isinstance(other, ListStarRocksDbParametersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
