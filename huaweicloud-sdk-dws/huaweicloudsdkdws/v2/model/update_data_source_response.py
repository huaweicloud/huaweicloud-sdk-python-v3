# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDataSourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'data_source_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'data_source_id': 'data_source_id'
    }

    def __init__(self, job_id=None, data_source_id=None):
        r"""UpdateDataSourceResponse

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**： 更新数据源任务ID。 **取值范围**： 不涉及。
        :type job_id: str
        :param data_source_id: **参数解释**： 数据源ID。 **取值范围**： 不涉及。
        :type data_source_id: str
        """
        
        super(UpdateDataSourceResponse, self).__init__()

        self._job_id = None
        self._data_source_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if data_source_id is not None:
            self.data_source_id = data_source_id

    @property
    def job_id(self):
        r"""Gets the job_id of this UpdateDataSourceResponse.

        **参数解释**： 更新数据源任务ID。 **取值范围**： 不涉及。

        :return: The job_id of this UpdateDataSourceResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this UpdateDataSourceResponse.

        **参数解释**： 更新数据源任务ID。 **取值范围**： 不涉及。

        :param job_id: The job_id of this UpdateDataSourceResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def data_source_id(self):
        r"""Gets the data_source_id of this UpdateDataSourceResponse.

        **参数解释**： 数据源ID。 **取值范围**： 不涉及。

        :return: The data_source_id of this UpdateDataSourceResponse.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        r"""Sets the data_source_id of this UpdateDataSourceResponse.

        **参数解释**： 数据源ID。 **取值范围**： 不涉及。

        :param data_source_id: The data_source_id of this UpdateDataSourceResponse.
        :type data_source_id: str
        """
        self._data_source_id = data_source_id

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
        if not isinstance(other, UpdateDataSourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
