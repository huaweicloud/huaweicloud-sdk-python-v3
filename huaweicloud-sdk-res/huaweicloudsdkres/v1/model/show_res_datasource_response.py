# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResDatasourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'datasource': 'Datasources',
        'jobs': 'list[Jobs]',
        'is_success': 'bool',
        'message': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'datasource': 'datasource',
        'jobs': 'jobs',
        'is_success': 'is_success',
        'message': 'message',
        'error_code': 'error_code'
    }

    def __init__(self, datasource=None, jobs=None, is_success=None, message=None, error_code=None):
        """ShowResDatasourceResponse

        The model defined in huaweicloud sdk

        :param datasource: 
        :type datasource: :class:`huaweicloudsdkres.v1.Datasources`
        :param jobs: 数据源相关任务详情。
        :type jobs: list[:class:`huaweicloudsdkres.v1.Jobs`]
        :param is_success: 是否成功。
        :type is_success: bool
        :param message: 返回消息（请求成功时，不返回此字段）。
        :type message: str
        :param error_code: 错误码（请求成功时，不返回此字段）。
        :type error_code: str
        """
        
        super(ShowResDatasourceResponse, self).__init__()

        self._datasource = None
        self._jobs = None
        self._is_success = None
        self._message = None
        self._error_code = None
        self.discriminator = None

        if datasource is not None:
            self.datasource = datasource
        if jobs is not None:
            self.jobs = jobs
        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if error_code is not None:
            self.error_code = error_code

    @property
    def datasource(self):
        """Gets the datasource of this ShowResDatasourceResponse.


        :return: The datasource of this ShowResDatasourceResponse.
        :rtype: :class:`huaweicloudsdkres.v1.Datasources`
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """Sets the datasource of this ShowResDatasourceResponse.


        :param datasource: The datasource of this ShowResDatasourceResponse.
        :type datasource: :class:`huaweicloudsdkres.v1.Datasources`
        """
        self._datasource = datasource

    @property
    def jobs(self):
        """Gets the jobs of this ShowResDatasourceResponse.

        数据源相关任务详情。

        :return: The jobs of this ShowResDatasourceResponse.
        :rtype: list[:class:`huaweicloudsdkres.v1.Jobs`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ShowResDatasourceResponse.

        数据源相关任务详情。

        :param jobs: The jobs of this ShowResDatasourceResponse.
        :type jobs: list[:class:`huaweicloudsdkres.v1.Jobs`]
        """
        self._jobs = jobs

    @property
    def is_success(self):
        """Gets the is_success of this ShowResDatasourceResponse.

        是否成功。

        :return: The is_success of this ShowResDatasourceResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ShowResDatasourceResponse.

        是否成功。

        :param is_success: The is_success of this ShowResDatasourceResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ShowResDatasourceResponse.

        返回消息（请求成功时，不返回此字段）。

        :return: The message of this ShowResDatasourceResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowResDatasourceResponse.

        返回消息（请求成功时，不返回此字段）。

        :param message: The message of this ShowResDatasourceResponse.
        :type message: str
        """
        self._message = message

    @property
    def error_code(self):
        """Gets the error_code of this ShowResDatasourceResponse.

        错误码（请求成功时，不返回此字段）。

        :return: The error_code of this ShowResDatasourceResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ShowResDatasourceResponse.

        错误码（请求成功时，不返回此字段）。

        :param error_code: The error_code of this ShowResDatasourceResponse.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, ShowResDatasourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
