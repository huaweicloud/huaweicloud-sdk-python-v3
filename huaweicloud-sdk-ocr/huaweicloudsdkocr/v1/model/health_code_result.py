# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthCodeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'name': 'str',
        'idcard_number': 'str',
        'phone_number': 'str',
        'province': 'str',
        'city': 'str',
        'time': 'str',
        'color': 'str',
        'vaccination_status': 'str',
        'test_interval': 'str',
        'pcr_test_result': 'str',
        'pcr_test_organization': 'str',
        'pcr_test_time': 'str',
        'pcr_sampling_time': 'str',
        'reached_city': 'list[str]',
        'confidence': 'object',
        'words_block_count': 'int',
        'words_block_list': 'list[HealthCodeWordsBlockList]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'idcard_number': 'idcard_number',
        'phone_number': 'phone_number',
        'province': 'province',
        'city': 'city',
        'time': 'time',
        'color': 'color',
        'vaccination_status': 'vaccination_status',
        'test_interval': 'test_interval',
        'pcr_test_result': 'pcr_test_result',
        'pcr_test_organization': 'pcr_test_organization',
        'pcr_test_time': 'pcr_test_time',
        'pcr_sampling_time': 'pcr_sampling_time',
        'reached_city': 'reached_city',
        'confidence': 'confidence',
        'words_block_count': 'words_block_count',
        'words_block_list': 'words_block_list'
    }

    def __init__(self, type=None, name=None, idcard_number=None, phone_number=None, province=None, city=None, time=None, color=None, vaccination_status=None, test_interval=None, pcr_test_result=None, pcr_test_organization=None, pcr_test_time=None, pcr_sampling_time=None, reached_city=None, confidence=None, words_block_count=None, words_block_list=None):
        r"""HealthCodeResult

        The model defined in huaweicloud sdk

        :param type: 防疫码类别： - 健康码：health_code - 核酸检测记录：pcr_test_record - 通信行程卡：travel_card - 其他：other 
        :type type: str
        :param name: 姓名 
        :type name: str
        :param idcard_number: 身份证号码 
        :type idcard_number: str
        :param phone_number: 手机号码 
        :type phone_number: str
        :param province: 省份 
        :type province: str
        :param city: 城市 
        :type city: str
        :param time: 健康码或行程卡的更新时间 
        :type time: str
        :param color: 健康码或行程卡颜色。 健康码颜色可选值包括：  - \&quot;green\&quot;，绿码 - \&quot;yellow\&quot;，黄码 - \&quot;red\&quot;，红码 - \&quot;gray\&quot;，灰码  行程卡颜色可选值包括：  - \&quot;green\&quot;，绿码 - \&quot;yellow\&quot;，黄码 - \&quot;red\&quot;，红码 
        :type color: str
        :param vaccination_status: 疫苗接种情况，可选值包括：  - 未接种 - 接种中 - 无接种记录 - 已接种1针 - 已接种2针 - 已接种3针 - 已完成新冠疫苗接种 
        :type vaccination_status: str
        :param test_interval: 核酸检测间隔时长，可选值包括： - 24小时内 - 48小时内 - 72小时内 - 5天内 - 7天内 - 7天外 
        :type test_interval: str
        :param pcr_test_result: 核酸检测结果，可选值包括： - \&quot;positive\&quot;,即阳性 - \&quot;negative\&quot;,即阴性 - \&quot;unknown\&quot;,未知 
        :type pcr_test_result: str
        :param pcr_test_organization: 核酸检测机构 
        :type pcr_test_organization: str
        :param pcr_test_time: 核酸检测结果更新时间 
        :type pcr_test_time: str
        :param pcr_sampling_time: 核酸检测采样时间 
        :type pcr_sampling_time: str
        :param reached_city: 行程卡的途径地址 
        :type reached_city: list[str]
        :param confidence: 各个字段的置信度。 
        :type confidence: object
        :param words_block_count: 代表检测识别出来的文字块数目。 
        :type words_block_count: int
        :param words_block_list: 识别文字块列表，输出顺序从左到右，从上到下。 
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.HealthCodeWordsBlockList`]
        """
        
        

        self._type = None
        self._name = None
        self._idcard_number = None
        self._phone_number = None
        self._province = None
        self._city = None
        self._time = None
        self._color = None
        self._vaccination_status = None
        self._test_interval = None
        self._pcr_test_result = None
        self._pcr_test_organization = None
        self._pcr_test_time = None
        self._pcr_sampling_time = None
        self._reached_city = None
        self._confidence = None
        self._words_block_count = None
        self._words_block_list = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.idcard_number = idcard_number
        self.phone_number = phone_number
        self.province = province
        self.city = city
        self.time = time
        self.color = color
        self.vaccination_status = vaccination_status
        self.test_interval = test_interval
        self.pcr_test_result = pcr_test_result
        self.pcr_test_organization = pcr_test_organization
        self.pcr_test_time = pcr_test_time
        self.pcr_sampling_time = pcr_sampling_time
        self.reached_city = reached_city
        self.confidence = confidence
        self.words_block_count = words_block_count
        self.words_block_list = words_block_list

    @property
    def type(self):
        r"""Gets the type of this HealthCodeResult.

        防疫码类别： - 健康码：health_code - 核酸检测记录：pcr_test_record - 通信行程卡：travel_card - 其他：other 

        :return: The type of this HealthCodeResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HealthCodeResult.

        防疫码类别： - 健康码：health_code - 核酸检测记录：pcr_test_record - 通信行程卡：travel_card - 其他：other 

        :param type: The type of this HealthCodeResult.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this HealthCodeResult.

        姓名 

        :return: The name of this HealthCodeResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HealthCodeResult.

        姓名 

        :param name: The name of this HealthCodeResult.
        :type name: str
        """
        self._name = name

    @property
    def idcard_number(self):
        r"""Gets the idcard_number of this HealthCodeResult.

        身份证号码 

        :return: The idcard_number of this HealthCodeResult.
        :rtype: str
        """
        return self._idcard_number

    @idcard_number.setter
    def idcard_number(self, idcard_number):
        r"""Sets the idcard_number of this HealthCodeResult.

        身份证号码 

        :param idcard_number: The idcard_number of this HealthCodeResult.
        :type idcard_number: str
        """
        self._idcard_number = idcard_number

    @property
    def phone_number(self):
        r"""Gets the phone_number of this HealthCodeResult.

        手机号码 

        :return: The phone_number of this HealthCodeResult.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        r"""Sets the phone_number of this HealthCodeResult.

        手机号码 

        :param phone_number: The phone_number of this HealthCodeResult.
        :type phone_number: str
        """
        self._phone_number = phone_number

    @property
    def province(self):
        r"""Gets the province of this HealthCodeResult.

        省份 

        :return: The province of this HealthCodeResult.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this HealthCodeResult.

        省份 

        :param province: The province of this HealthCodeResult.
        :type province: str
        """
        self._province = province

    @property
    def city(self):
        r"""Gets the city of this HealthCodeResult.

        城市 

        :return: The city of this HealthCodeResult.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this HealthCodeResult.

        城市 

        :param city: The city of this HealthCodeResult.
        :type city: str
        """
        self._city = city

    @property
    def time(self):
        r"""Gets the time of this HealthCodeResult.

        健康码或行程卡的更新时间 

        :return: The time of this HealthCodeResult.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this HealthCodeResult.

        健康码或行程卡的更新时间 

        :param time: The time of this HealthCodeResult.
        :type time: str
        """
        self._time = time

    @property
    def color(self):
        r"""Gets the color of this HealthCodeResult.

        健康码或行程卡颜色。 健康码颜色可选值包括：  - \"green\"，绿码 - \"yellow\"，黄码 - \"red\"，红码 - \"gray\"，灰码  行程卡颜色可选值包括：  - \"green\"，绿码 - \"yellow\"，黄码 - \"red\"，红码 

        :return: The color of this HealthCodeResult.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this HealthCodeResult.

        健康码或行程卡颜色。 健康码颜色可选值包括：  - \"green\"，绿码 - \"yellow\"，黄码 - \"red\"，红码 - \"gray\"，灰码  行程卡颜色可选值包括：  - \"green\"，绿码 - \"yellow\"，黄码 - \"red\"，红码 

        :param color: The color of this HealthCodeResult.
        :type color: str
        """
        self._color = color

    @property
    def vaccination_status(self):
        r"""Gets the vaccination_status of this HealthCodeResult.

        疫苗接种情况，可选值包括：  - 未接种 - 接种中 - 无接种记录 - 已接种1针 - 已接种2针 - 已接种3针 - 已完成新冠疫苗接种 

        :return: The vaccination_status of this HealthCodeResult.
        :rtype: str
        """
        return self._vaccination_status

    @vaccination_status.setter
    def vaccination_status(self, vaccination_status):
        r"""Sets the vaccination_status of this HealthCodeResult.

        疫苗接种情况，可选值包括：  - 未接种 - 接种中 - 无接种记录 - 已接种1针 - 已接种2针 - 已接种3针 - 已完成新冠疫苗接种 

        :param vaccination_status: The vaccination_status of this HealthCodeResult.
        :type vaccination_status: str
        """
        self._vaccination_status = vaccination_status

    @property
    def test_interval(self):
        r"""Gets the test_interval of this HealthCodeResult.

        核酸检测间隔时长，可选值包括： - 24小时内 - 48小时内 - 72小时内 - 5天内 - 7天内 - 7天外 

        :return: The test_interval of this HealthCodeResult.
        :rtype: str
        """
        return self._test_interval

    @test_interval.setter
    def test_interval(self, test_interval):
        r"""Sets the test_interval of this HealthCodeResult.

        核酸检测间隔时长，可选值包括： - 24小时内 - 48小时内 - 72小时内 - 5天内 - 7天内 - 7天外 

        :param test_interval: The test_interval of this HealthCodeResult.
        :type test_interval: str
        """
        self._test_interval = test_interval

    @property
    def pcr_test_result(self):
        r"""Gets the pcr_test_result of this HealthCodeResult.

        核酸检测结果，可选值包括： - \"positive\",即阳性 - \"negative\",即阴性 - \"unknown\",未知 

        :return: The pcr_test_result of this HealthCodeResult.
        :rtype: str
        """
        return self._pcr_test_result

    @pcr_test_result.setter
    def pcr_test_result(self, pcr_test_result):
        r"""Sets the pcr_test_result of this HealthCodeResult.

        核酸检测结果，可选值包括： - \"positive\",即阳性 - \"negative\",即阴性 - \"unknown\",未知 

        :param pcr_test_result: The pcr_test_result of this HealthCodeResult.
        :type pcr_test_result: str
        """
        self._pcr_test_result = pcr_test_result

    @property
    def pcr_test_organization(self):
        r"""Gets the pcr_test_organization of this HealthCodeResult.

        核酸检测机构 

        :return: The pcr_test_organization of this HealthCodeResult.
        :rtype: str
        """
        return self._pcr_test_organization

    @pcr_test_organization.setter
    def pcr_test_organization(self, pcr_test_organization):
        r"""Sets the pcr_test_organization of this HealthCodeResult.

        核酸检测机构 

        :param pcr_test_organization: The pcr_test_organization of this HealthCodeResult.
        :type pcr_test_organization: str
        """
        self._pcr_test_organization = pcr_test_organization

    @property
    def pcr_test_time(self):
        r"""Gets the pcr_test_time of this HealthCodeResult.

        核酸检测结果更新时间 

        :return: The pcr_test_time of this HealthCodeResult.
        :rtype: str
        """
        return self._pcr_test_time

    @pcr_test_time.setter
    def pcr_test_time(self, pcr_test_time):
        r"""Sets the pcr_test_time of this HealthCodeResult.

        核酸检测结果更新时间 

        :param pcr_test_time: The pcr_test_time of this HealthCodeResult.
        :type pcr_test_time: str
        """
        self._pcr_test_time = pcr_test_time

    @property
    def pcr_sampling_time(self):
        r"""Gets the pcr_sampling_time of this HealthCodeResult.

        核酸检测采样时间 

        :return: The pcr_sampling_time of this HealthCodeResult.
        :rtype: str
        """
        return self._pcr_sampling_time

    @pcr_sampling_time.setter
    def pcr_sampling_time(self, pcr_sampling_time):
        r"""Sets the pcr_sampling_time of this HealthCodeResult.

        核酸检测采样时间 

        :param pcr_sampling_time: The pcr_sampling_time of this HealthCodeResult.
        :type pcr_sampling_time: str
        """
        self._pcr_sampling_time = pcr_sampling_time

    @property
    def reached_city(self):
        r"""Gets the reached_city of this HealthCodeResult.

        行程卡的途径地址 

        :return: The reached_city of this HealthCodeResult.
        :rtype: list[str]
        """
        return self._reached_city

    @reached_city.setter
    def reached_city(self, reached_city):
        r"""Sets the reached_city of this HealthCodeResult.

        行程卡的途径地址 

        :param reached_city: The reached_city of this HealthCodeResult.
        :type reached_city: list[str]
        """
        self._reached_city = reached_city

    @property
    def confidence(self):
        r"""Gets the confidence of this HealthCodeResult.

        各个字段的置信度。 

        :return: The confidence of this HealthCodeResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this HealthCodeResult.

        各个字段的置信度。 

        :param confidence: The confidence of this HealthCodeResult.
        :type confidence: object
        """
        self._confidence = confidence

    @property
    def words_block_count(self):
        r"""Gets the words_block_count of this HealthCodeResult.

        代表检测识别出来的文字块数目。 

        :return: The words_block_count of this HealthCodeResult.
        :rtype: int
        """
        return self._words_block_count

    @words_block_count.setter
    def words_block_count(self, words_block_count):
        r"""Sets the words_block_count of this HealthCodeResult.

        代表检测识别出来的文字块数目。 

        :param words_block_count: The words_block_count of this HealthCodeResult.
        :type words_block_count: int
        """
        self._words_block_count = words_block_count

    @property
    def words_block_list(self):
        r"""Gets the words_block_list of this HealthCodeResult.

        识别文字块列表，输出顺序从左到右，从上到下。 

        :return: The words_block_list of this HealthCodeResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.HealthCodeWordsBlockList`]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        r"""Sets the words_block_list of this HealthCodeResult.

        识别文字块列表，输出顺序从左到右，从上到下。 

        :param words_block_list: The words_block_list of this HealthCodeResult.
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.HealthCodeWordsBlockList`]
        """
        self._words_block_list = words_block_list

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
        if not isinstance(other, HealthCodeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
