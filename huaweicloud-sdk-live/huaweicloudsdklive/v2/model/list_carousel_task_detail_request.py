# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCarouselTaskDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'carousel_task_id': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'carousel_task_id': 'carousel_task_id',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, carousel_task_id=None, start_time=None, end_time=None):
        r"""ListCarouselTaskDetailRequest

        The model defined in huaweicloud sdk

        :param carousel_task_id: 轮播任务id。 
        :type carousel_task_id: str
        :param start_time: 起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度3小时，最大查询周期7天。  若参数为空，默认查询最近1小时数据。 
        :type start_time: str
        :param end_time: 结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度3小时，最大查询周期7天。  若参数为空，默认为当前时间。结束时间需大于起始时间。 
        :type end_time: str
        """
        
        

        self._carousel_task_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.carousel_task_id = carousel_task_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def carousel_task_id(self):
        r"""Gets the carousel_task_id of this ListCarouselTaskDetailRequest.

        轮播任务id。 

        :return: The carousel_task_id of this ListCarouselTaskDetailRequest.
        :rtype: str
        """
        return self._carousel_task_id

    @carousel_task_id.setter
    def carousel_task_id(self, carousel_task_id):
        r"""Sets the carousel_task_id of this ListCarouselTaskDetailRequest.

        轮播任务id。 

        :param carousel_task_id: The carousel_task_id of this ListCarouselTaskDetailRequest.
        :type carousel_task_id: str
        """
        self._carousel_task_id = carousel_task_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListCarouselTaskDetailRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度3小时，最大查询周期7天。  若参数为空，默认查询最近1小时数据。 

        :return: The start_time of this ListCarouselTaskDetailRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListCarouselTaskDetailRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度3小时，最大查询周期7天。  若参数为空，默认查询最近1小时数据。 

        :param start_time: The start_time of this ListCarouselTaskDetailRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListCarouselTaskDetailRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度3小时，最大查询周期7天。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :return: The end_time of this ListCarouselTaskDetailRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListCarouselTaskDetailRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度3小时，最大查询周期7天。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :param end_time: The end_time of this ListCarouselTaskDetailRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListCarouselTaskDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
