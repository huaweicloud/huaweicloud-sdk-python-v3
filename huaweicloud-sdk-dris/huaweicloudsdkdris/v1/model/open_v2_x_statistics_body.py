# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenV2XStatisticsBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'StatisticsSourceDTO',
        'time': 'str',
        'period': 'int',
        'direction': 'float',
        'flow': 'int',
        'average_speed': 'float',
        'esn': 'str',
        'cross_id': 'str',
        'traffic_direction': 'int',
        'road_kind': 'int',
        'vehicle_class_flow': 'list[ModelFlow]',
        'occupancy': 'list[LaneOccupancy]'
    }

    attribute_map = {
        'source': 'source',
        'time': 'time',
        'period': 'period',
        'direction': 'direction',
        'flow': 'flow',
        'average_speed': 'average_speed',
        'esn': 'esn',
        'cross_id': 'cross_id',
        'traffic_direction': 'traffic_direction',
        'road_kind': 'road_kind',
        'vehicle_class_flow': 'vehicle_class_flow',
        'occupancy': 'occupancy'
    }

    def __init__(self, source=None, time=None, period=None, direction=None, flow=None, average_speed=None, esn=None, cross_id=None, traffic_direction=None, road_kind=None, vehicle_class_flow=None, occupancy=None):
        """OpenV2XStatisticsBody

        The model defined in huaweicloud sdk

        :param source: 
        :type source: :class:`huaweicloudsdkdris.v1.StatisticsSourceDTO`
        :param time: **参数说明**：数据上报的时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;。 例如：2021-01-08T02:03:41Z。 
        :type time: str
        :param period: **参数说明**：统计周期，单位秒。
        :type period: int
        :param direction: **参数说明**：道路路的角度，区分道路方向，向东为0度，逆时针增加。
        :type direction: float
        :param flow: **参数说明**：统计周期内的车辆数。
        :type flow: int
        :param average_speed: **参数说明**：车辆平均速度，单位km/h。
        :type average_speed: float
        :param esn: **参数说明**：设备编码。 **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。 
        :type esn: str
        :param cross_id: **参数说明**：路口id，对应到一组雷视拟合设备，检测一个特定的路口或者路段。
        :type cross_id: str
        :param traffic_direction: **参数说明**：路段的交通流方向，交通流方向按照“西北规则”进行定义，即尽量选择西北的点作为正向起点，先西后北。西北规则具体说明请参见 [“西北规则”说明](此处添加support文档的url)。 0：正向 1：逆向 2：正向转逆向的连接线 3：逆向转正向的连接线 9：为方向未确定 
        :type traffic_direction: int
        :param road_kind: **参数说明**：道路特征，0为主路，1为汇入匝道，2为汇出匝道，3为辅道
        :type road_kind: int
        :param vehicle_class_flow: **参数说明**：不同车辆类型的流量统计。
        :type vehicle_class_flow: list[:class:`huaweicloudsdkdris.v1.ModelFlow`]
        :param occupancy: **参数说明**：分车道统计的占有率列表。
        :type occupancy: list[:class:`huaweicloudsdkdris.v1.LaneOccupancy`]
        """
        
        

        self._source = None
        self._time = None
        self._period = None
        self._direction = None
        self._flow = None
        self._average_speed = None
        self._esn = None
        self._cross_id = None
        self._traffic_direction = None
        self._road_kind = None
        self._vehicle_class_flow = None
        self._occupancy = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if time is not None:
            self.time = time
        if period is not None:
            self.period = period
        if direction is not None:
            self.direction = direction
        if flow is not None:
            self.flow = flow
        if average_speed is not None:
            self.average_speed = average_speed
        if esn is not None:
            self.esn = esn
        if cross_id is not None:
            self.cross_id = cross_id
        if traffic_direction is not None:
            self.traffic_direction = traffic_direction
        if road_kind is not None:
            self.road_kind = road_kind
        if vehicle_class_flow is not None:
            self.vehicle_class_flow = vehicle_class_flow
        if occupancy is not None:
            self.occupancy = occupancy

    @property
    def source(self):
        """Gets the source of this OpenV2XStatisticsBody.

        :return: The source of this OpenV2XStatisticsBody.
        :rtype: :class:`huaweicloudsdkdris.v1.StatisticsSourceDTO`
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this OpenV2XStatisticsBody.

        :param source: The source of this OpenV2XStatisticsBody.
        :type source: :class:`huaweicloudsdkdris.v1.StatisticsSourceDTO`
        """
        self._source = source

    @property
    def time(self):
        """Gets the time of this OpenV2XStatisticsBody.

        **参数说明**：数据上报的时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'。 例如：2021-01-08T02:03:41Z。 

        :return: The time of this OpenV2XStatisticsBody.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OpenV2XStatisticsBody.

        **参数说明**：数据上报的时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'。 例如：2021-01-08T02:03:41Z。 

        :param time: The time of this OpenV2XStatisticsBody.
        :type time: str
        """
        self._time = time

    @property
    def period(self):
        """Gets the period of this OpenV2XStatisticsBody.

        **参数说明**：统计周期，单位秒。

        :return: The period of this OpenV2XStatisticsBody.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this OpenV2XStatisticsBody.

        **参数说明**：统计周期，单位秒。

        :param period: The period of this OpenV2XStatisticsBody.
        :type period: int
        """
        self._period = period

    @property
    def direction(self):
        """Gets the direction of this OpenV2XStatisticsBody.

        **参数说明**：道路路的角度，区分道路方向，向东为0度，逆时针增加。

        :return: The direction of this OpenV2XStatisticsBody.
        :rtype: float
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this OpenV2XStatisticsBody.

        **参数说明**：道路路的角度，区分道路方向，向东为0度，逆时针增加。

        :param direction: The direction of this OpenV2XStatisticsBody.
        :type direction: float
        """
        self._direction = direction

    @property
    def flow(self):
        """Gets the flow of this OpenV2XStatisticsBody.

        **参数说明**：统计周期内的车辆数。

        :return: The flow of this OpenV2XStatisticsBody.
        :rtype: int
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this OpenV2XStatisticsBody.

        **参数说明**：统计周期内的车辆数。

        :param flow: The flow of this OpenV2XStatisticsBody.
        :type flow: int
        """
        self._flow = flow

    @property
    def average_speed(self):
        """Gets the average_speed of this OpenV2XStatisticsBody.

        **参数说明**：车辆平均速度，单位km/h。

        :return: The average_speed of this OpenV2XStatisticsBody.
        :rtype: float
        """
        return self._average_speed

    @average_speed.setter
    def average_speed(self, average_speed):
        """Sets the average_speed of this OpenV2XStatisticsBody.

        **参数说明**：车辆平均速度，单位km/h。

        :param average_speed: The average_speed of this OpenV2XStatisticsBody.
        :type average_speed: float
        """
        self._average_speed = average_speed

    @property
    def esn(self):
        """Gets the esn of this OpenV2XStatisticsBody.

        **参数说明**：设备编码。 **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。 

        :return: The esn of this OpenV2XStatisticsBody.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """Sets the esn of this OpenV2XStatisticsBody.

        **参数说明**：设备编码。 **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。 

        :param esn: The esn of this OpenV2XStatisticsBody.
        :type esn: str
        """
        self._esn = esn

    @property
    def cross_id(self):
        """Gets the cross_id of this OpenV2XStatisticsBody.

        **参数说明**：路口id，对应到一组雷视拟合设备，检测一个特定的路口或者路段。

        :return: The cross_id of this OpenV2XStatisticsBody.
        :rtype: str
        """
        return self._cross_id

    @cross_id.setter
    def cross_id(self, cross_id):
        """Sets the cross_id of this OpenV2XStatisticsBody.

        **参数说明**：路口id，对应到一组雷视拟合设备，检测一个特定的路口或者路段。

        :param cross_id: The cross_id of this OpenV2XStatisticsBody.
        :type cross_id: str
        """
        self._cross_id = cross_id

    @property
    def traffic_direction(self):
        """Gets the traffic_direction of this OpenV2XStatisticsBody.

        **参数说明**：路段的交通流方向，交通流方向按照“西北规则”进行定义，即尽量选择西北的点作为正向起点，先西后北。西北规则具体说明请参见 [“西北规则”说明](此处添加support文档的url)。 0：正向 1：逆向 2：正向转逆向的连接线 3：逆向转正向的连接线 9：为方向未确定 

        :return: The traffic_direction of this OpenV2XStatisticsBody.
        :rtype: int
        """
        return self._traffic_direction

    @traffic_direction.setter
    def traffic_direction(self, traffic_direction):
        """Sets the traffic_direction of this OpenV2XStatisticsBody.

        **参数说明**：路段的交通流方向，交通流方向按照“西北规则”进行定义，即尽量选择西北的点作为正向起点，先西后北。西北规则具体说明请参见 [“西北规则”说明](此处添加support文档的url)。 0：正向 1：逆向 2：正向转逆向的连接线 3：逆向转正向的连接线 9：为方向未确定 

        :param traffic_direction: The traffic_direction of this OpenV2XStatisticsBody.
        :type traffic_direction: int
        """
        self._traffic_direction = traffic_direction

    @property
    def road_kind(self):
        """Gets the road_kind of this OpenV2XStatisticsBody.

        **参数说明**：道路特征，0为主路，1为汇入匝道，2为汇出匝道，3为辅道

        :return: The road_kind of this OpenV2XStatisticsBody.
        :rtype: int
        """
        return self._road_kind

    @road_kind.setter
    def road_kind(self, road_kind):
        """Sets the road_kind of this OpenV2XStatisticsBody.

        **参数说明**：道路特征，0为主路，1为汇入匝道，2为汇出匝道，3为辅道

        :param road_kind: The road_kind of this OpenV2XStatisticsBody.
        :type road_kind: int
        """
        self._road_kind = road_kind

    @property
    def vehicle_class_flow(self):
        """Gets the vehicle_class_flow of this OpenV2XStatisticsBody.

        **参数说明**：不同车辆类型的流量统计。

        :return: The vehicle_class_flow of this OpenV2XStatisticsBody.
        :rtype: list[:class:`huaweicloudsdkdris.v1.ModelFlow`]
        """
        return self._vehicle_class_flow

    @vehicle_class_flow.setter
    def vehicle_class_flow(self, vehicle_class_flow):
        """Sets the vehicle_class_flow of this OpenV2XStatisticsBody.

        **参数说明**：不同车辆类型的流量统计。

        :param vehicle_class_flow: The vehicle_class_flow of this OpenV2XStatisticsBody.
        :type vehicle_class_flow: list[:class:`huaweicloudsdkdris.v1.ModelFlow`]
        """
        self._vehicle_class_flow = vehicle_class_flow

    @property
    def occupancy(self):
        """Gets the occupancy of this OpenV2XStatisticsBody.

        **参数说明**：分车道统计的占有率列表。

        :return: The occupancy of this OpenV2XStatisticsBody.
        :rtype: list[:class:`huaweicloudsdkdris.v1.LaneOccupancy`]
        """
        return self._occupancy

    @occupancy.setter
    def occupancy(self, occupancy):
        """Sets the occupancy of this OpenV2XStatisticsBody.

        **参数说明**：分车道统计的占有率列表。

        :param occupancy: The occupancy of this OpenV2XStatisticsBody.
        :type occupancy: list[:class:`huaweicloudsdkdris.v1.LaneOccupancy`]
        """
        self._occupancy = occupancy

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
        if not isinstance(other, OpenV2XStatisticsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
