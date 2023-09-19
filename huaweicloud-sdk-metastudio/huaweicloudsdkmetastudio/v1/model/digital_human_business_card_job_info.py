# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DigitalHumanBusinessCardJobInfo:

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
        'state': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'output_asset_config': 'OutputAssetInfo',
        'error_info': 'ErrorResponse',
        'create_time': 'str',
        'lastupdate_time': 'str',
        'business_card_type': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'state': 'state',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'output_asset_config': 'output_asset_config',
        'error_info': 'error_info',
        'create_time': 'create_time',
        'lastupdate_time': 'lastupdate_time',
        'business_card_type': 'business_card_type'
    }

    def __init__(self, job_id=None, state=None, start_time=None, end_time=None, output_asset_config=None, error_info=None, create_time=None, lastupdate_time=None, business_card_type=None):
        """DigitalHumanBusinessCardJobInfo

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param state: 任务的状态。 * WAITING: 等待 * PROCESSING: 处理中 * SUCCEED: 成功 * FAILED: 失败 * CANCELED: 取消
        :type state: str
        :param start_time: 数字人名片制作开始时间。
        :type start_time: str
        :param end_time: 数字人名片制作结束时间。
        :type end_time: str
        :param output_asset_config: 
        :type output_asset_config: :class:`huaweicloudsdkmetastudio.v1.OutputAssetInfo`
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        :param create_time: 任务创建时间。
        :type create_time: str
        :param lastupdate_time: 任务更新时间。
        :type lastupdate_time: str
        :param business_card_type: 数字人名片类型。 * 2D_DIGITAL_HUMAN_CARD：分身数字人名片
        :type business_card_type: str
        """
        
        

        self._job_id = None
        self._state = None
        self._start_time = None
        self._end_time = None
        self._output_asset_config = None
        self._error_info = None
        self._create_time = None
        self._lastupdate_time = None
        self._business_card_type = None
        self.discriminator = None

        self.job_id = job_id
        self.state = state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if output_asset_config is not None:
            self.output_asset_config = output_asset_config
        if error_info is not None:
            self.error_info = error_info
        if create_time is not None:
            self.create_time = create_time
        if lastupdate_time is not None:
            self.lastupdate_time = lastupdate_time
        if business_card_type is not None:
            self.business_card_type = business_card_type

    @property
    def job_id(self):
        """Gets the job_id of this DigitalHumanBusinessCardJobInfo.

        任务ID。

        :return: The job_id of this DigitalHumanBusinessCardJobInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DigitalHumanBusinessCardJobInfo.

        任务ID。

        :param job_id: The job_id of this DigitalHumanBusinessCardJobInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        """Gets the state of this DigitalHumanBusinessCardJobInfo.

        任务的状态。 * WAITING: 等待 * PROCESSING: 处理中 * SUCCEED: 成功 * FAILED: 失败 * CANCELED: 取消

        :return: The state of this DigitalHumanBusinessCardJobInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DigitalHumanBusinessCardJobInfo.

        任务的状态。 * WAITING: 等待 * PROCESSING: 处理中 * SUCCEED: 成功 * FAILED: 失败 * CANCELED: 取消

        :param state: The state of this DigitalHumanBusinessCardJobInfo.
        :type state: str
        """
        self._state = state

    @property
    def start_time(self):
        """Gets the start_time of this DigitalHumanBusinessCardJobInfo.

        数字人名片制作开始时间。

        :return: The start_time of this DigitalHumanBusinessCardJobInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DigitalHumanBusinessCardJobInfo.

        数字人名片制作开始时间。

        :param start_time: The start_time of this DigitalHumanBusinessCardJobInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this DigitalHumanBusinessCardJobInfo.

        数字人名片制作结束时间。

        :return: The end_time of this DigitalHumanBusinessCardJobInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DigitalHumanBusinessCardJobInfo.

        数字人名片制作结束时间。

        :param end_time: The end_time of this DigitalHumanBusinessCardJobInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def output_asset_config(self):
        """Gets the output_asset_config of this DigitalHumanBusinessCardJobInfo.

        :return: The output_asset_config of this DigitalHumanBusinessCardJobInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.OutputAssetInfo`
        """
        return self._output_asset_config

    @output_asset_config.setter
    def output_asset_config(self, output_asset_config):
        """Sets the output_asset_config of this DigitalHumanBusinessCardJobInfo.

        :param output_asset_config: The output_asset_config of this DigitalHumanBusinessCardJobInfo.
        :type output_asset_config: :class:`huaweicloudsdkmetastudio.v1.OutputAssetInfo`
        """
        self._output_asset_config = output_asset_config

    @property
    def error_info(self):
        """Gets the error_info of this DigitalHumanBusinessCardJobInfo.

        :return: The error_info of this DigitalHumanBusinessCardJobInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """Sets the error_info of this DigitalHumanBusinessCardJobInfo.

        :param error_info: The error_info of this DigitalHumanBusinessCardJobInfo.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

    @property
    def create_time(self):
        """Gets the create_time of this DigitalHumanBusinessCardJobInfo.

        任务创建时间。

        :return: The create_time of this DigitalHumanBusinessCardJobInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DigitalHumanBusinessCardJobInfo.

        任务创建时间。

        :param create_time: The create_time of this DigitalHumanBusinessCardJobInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def lastupdate_time(self):
        """Gets the lastupdate_time of this DigitalHumanBusinessCardJobInfo.

        任务更新时间。

        :return: The lastupdate_time of this DigitalHumanBusinessCardJobInfo.
        :rtype: str
        """
        return self._lastupdate_time

    @lastupdate_time.setter
    def lastupdate_time(self, lastupdate_time):
        """Sets the lastupdate_time of this DigitalHumanBusinessCardJobInfo.

        任务更新时间。

        :param lastupdate_time: The lastupdate_time of this DigitalHumanBusinessCardJobInfo.
        :type lastupdate_time: str
        """
        self._lastupdate_time = lastupdate_time

    @property
    def business_card_type(self):
        """Gets the business_card_type of this DigitalHumanBusinessCardJobInfo.

        数字人名片类型。 * 2D_DIGITAL_HUMAN_CARD：分身数字人名片

        :return: The business_card_type of this DigitalHumanBusinessCardJobInfo.
        :rtype: str
        """
        return self._business_card_type

    @business_card_type.setter
    def business_card_type(self, business_card_type):
        """Sets the business_card_type of this DigitalHumanBusinessCardJobInfo.

        数字人名片类型。 * 2D_DIGITAL_HUMAN_CARD：分身数字人名片

        :param business_card_type: The business_card_type of this DigitalHumanBusinessCardJobInfo.
        :type business_card_type: str
        """
        self._business_card_type = business_card_type

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
        if not isinstance(other, DigitalHumanBusinessCardJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
