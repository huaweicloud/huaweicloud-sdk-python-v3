# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventParticipant:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ptc_type': 'str',
        'plate_no': 'str',
        'speed': 'int',
        'vehicle_class': 'int',
        'gat_vehicle_class': 'str',
        'track_id': 'int',
        'lane_no': 'int',
        'target_rects': 'list[TargetRect]'
    }

    attribute_map = {
        'ptc_type': 'ptc_type',
        'plate_no': 'plate_no',
        'speed': 'speed',
        'vehicle_class': 'vehicle_class',
        'gat_vehicle_class': 'gat_vehicle_class',
        'track_id': 'track_id',
        'lane_no': 'lane_no',
        'target_rects': 'target_rects'
    }

    def __init__(self, ptc_type=None, plate_no=None, speed=None, vehicle_class=None, gat_vehicle_class=None, track_id=None, lane_no=None, target_rects=None):
        """EventParticipant

        The model defined in huaweicloud sdk

        :param ptc_type: **参数说明**：交通参与者的具体类型描述。  **取值范围**：  - unknown：未知  - motor：机动车  - non-motor：非机动车  - pedestrian：行人 
        :type ptc_type: str
        :param plate_no: **参数说明**：车牌号。
        :type plate_no: str
        :param speed: **参数说明**：对应车辆被检测到超速或者慢行时的速度小。单位为0.02米每秒。值为8191时代表无效数值。
        :type speed: int
        :param vehicle_class: **参数说明**：车辆类型。参考 [车辆基本类型参数说明](https://support.huaweicloud.com/api-v2x/v2x_04_0162.html)。
        :type vehicle_class: int
        :param gat_vehicle_class: **参数说明**：机动车车辆类型。参考[机动车车辆类型](https://support.huaweicloud.com/api-v2x/v2x_04_0179.html)。
        :type gat_vehicle_class: str
        :param track_id: **参数说明**：感知设备识别的id，具体表示为机动车轨迹ID。
        :type track_id: int
        :param lane_no: **参数说明**：事件发生的所在车道
        :type lane_no: int
        :param target_rects: **参数说明**：目标检测框信息列表。
        :type target_rects: list[:class:`huaweicloudsdkdris.v1.TargetRect`]
        """
        
        

        self._ptc_type = None
        self._plate_no = None
        self._speed = None
        self._vehicle_class = None
        self._gat_vehicle_class = None
        self._track_id = None
        self._lane_no = None
        self._target_rects = None
        self.discriminator = None

        if ptc_type is not None:
            self.ptc_type = ptc_type
        if plate_no is not None:
            self.plate_no = plate_no
        if speed is not None:
            self.speed = speed
        if vehicle_class is not None:
            self.vehicle_class = vehicle_class
        if gat_vehicle_class is not None:
            self.gat_vehicle_class = gat_vehicle_class
        if track_id is not None:
            self.track_id = track_id
        if lane_no is not None:
            self.lane_no = lane_no
        if target_rects is not None:
            self.target_rects = target_rects

    @property
    def ptc_type(self):
        """Gets the ptc_type of this EventParticipant.

        **参数说明**：交通参与者的具体类型描述。  **取值范围**：  - unknown：未知  - motor：机动车  - non-motor：非机动车  - pedestrian：行人 

        :return: The ptc_type of this EventParticipant.
        :rtype: str
        """
        return self._ptc_type

    @ptc_type.setter
    def ptc_type(self, ptc_type):
        """Sets the ptc_type of this EventParticipant.

        **参数说明**：交通参与者的具体类型描述。  **取值范围**：  - unknown：未知  - motor：机动车  - non-motor：非机动车  - pedestrian：行人 

        :param ptc_type: The ptc_type of this EventParticipant.
        :type ptc_type: str
        """
        self._ptc_type = ptc_type

    @property
    def plate_no(self):
        """Gets the plate_no of this EventParticipant.

        **参数说明**：车牌号。

        :return: The plate_no of this EventParticipant.
        :rtype: str
        """
        return self._plate_no

    @plate_no.setter
    def plate_no(self, plate_no):
        """Sets the plate_no of this EventParticipant.

        **参数说明**：车牌号。

        :param plate_no: The plate_no of this EventParticipant.
        :type plate_no: str
        """
        self._plate_no = plate_no

    @property
    def speed(self):
        """Gets the speed of this EventParticipant.

        **参数说明**：对应车辆被检测到超速或者慢行时的速度小。单位为0.02米每秒。值为8191时代表无效数值。

        :return: The speed of this EventParticipant.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this EventParticipant.

        **参数说明**：对应车辆被检测到超速或者慢行时的速度小。单位为0.02米每秒。值为8191时代表无效数值。

        :param speed: The speed of this EventParticipant.
        :type speed: int
        """
        self._speed = speed

    @property
    def vehicle_class(self):
        """Gets the vehicle_class of this EventParticipant.

        **参数说明**：车辆类型。参考 [车辆基本类型参数说明](https://support.huaweicloud.com/api-v2x/v2x_04_0162.html)。

        :return: The vehicle_class of this EventParticipant.
        :rtype: int
        """
        return self._vehicle_class

    @vehicle_class.setter
    def vehicle_class(self, vehicle_class):
        """Sets the vehicle_class of this EventParticipant.

        **参数说明**：车辆类型。参考 [车辆基本类型参数说明](https://support.huaweicloud.com/api-v2x/v2x_04_0162.html)。

        :param vehicle_class: The vehicle_class of this EventParticipant.
        :type vehicle_class: int
        """
        self._vehicle_class = vehicle_class

    @property
    def gat_vehicle_class(self):
        """Gets the gat_vehicle_class of this EventParticipant.

        **参数说明**：机动车车辆类型。参考[机动车车辆类型](https://support.huaweicloud.com/api-v2x/v2x_04_0179.html)。

        :return: The gat_vehicle_class of this EventParticipant.
        :rtype: str
        """
        return self._gat_vehicle_class

    @gat_vehicle_class.setter
    def gat_vehicle_class(self, gat_vehicle_class):
        """Sets the gat_vehicle_class of this EventParticipant.

        **参数说明**：机动车车辆类型。参考[机动车车辆类型](https://support.huaweicloud.com/api-v2x/v2x_04_0179.html)。

        :param gat_vehicle_class: The gat_vehicle_class of this EventParticipant.
        :type gat_vehicle_class: str
        """
        self._gat_vehicle_class = gat_vehicle_class

    @property
    def track_id(self):
        """Gets the track_id of this EventParticipant.

        **参数说明**：感知设备识别的id，具体表示为机动车轨迹ID。

        :return: The track_id of this EventParticipant.
        :rtype: int
        """
        return self._track_id

    @track_id.setter
    def track_id(self, track_id):
        """Sets the track_id of this EventParticipant.

        **参数说明**：感知设备识别的id，具体表示为机动车轨迹ID。

        :param track_id: The track_id of this EventParticipant.
        :type track_id: int
        """
        self._track_id = track_id

    @property
    def lane_no(self):
        """Gets the lane_no of this EventParticipant.

        **参数说明**：事件发生的所在车道

        :return: The lane_no of this EventParticipant.
        :rtype: int
        """
        return self._lane_no

    @lane_no.setter
    def lane_no(self, lane_no):
        """Sets the lane_no of this EventParticipant.

        **参数说明**：事件发生的所在车道

        :param lane_no: The lane_no of this EventParticipant.
        :type lane_no: int
        """
        self._lane_no = lane_no

    @property
    def target_rects(self):
        """Gets the target_rects of this EventParticipant.

        **参数说明**：目标检测框信息列表。

        :return: The target_rects of this EventParticipant.
        :rtype: list[:class:`huaweicloudsdkdris.v1.TargetRect`]
        """
        return self._target_rects

    @target_rects.setter
    def target_rects(self, target_rects):
        """Sets the target_rects of this EventParticipant.

        **参数说明**：目标检测框信息列表。

        :param target_rects: The target_rects of this EventParticipant.
        :type target_rects: list[:class:`huaweicloudsdkdris.v1.TargetRect`]
        """
        self._target_rects = target_rects

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
        if not isinstance(other, EventParticipant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
