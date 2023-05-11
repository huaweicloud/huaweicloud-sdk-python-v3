# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrainTicketResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_id': 'str',
        'check_port': 'str',
        'train_number': 'str',
        'departure_station': 'str',
        'destination_station': 'str',
        'departure_station_en': 'str',
        'destination_station_en': 'str',
        'departure_time': 'str',
        'seat_number': 'str',
        'ticket_price': 'str',
        'sale_method': 'str',
        'seat_category': 'str',
        'ticket_changing': 'str',
        'id_number': 'str',
        'name': 'str',
        'log_id': 'str',
        'sale_location': 'str',
        'confidence': 'object',
        'text_location': 'object'
    }

    attribute_map = {
        'ticket_id': 'ticket_id',
        'check_port': 'check_port',
        'train_number': 'train_number',
        'departure_station': 'departure_station',
        'destination_station': 'destination_station',
        'departure_station_en': 'departure_station_en',
        'destination_station_en': 'destination_station_en',
        'departure_time': 'departure_time',
        'seat_number': 'seat_number',
        'ticket_price': 'ticket_price',
        'sale_method': 'sale_method',
        'seat_category': 'seat_category',
        'ticket_changing': 'ticket_changing',
        'id_number': 'id_number',
        'name': 'name',
        'log_id': 'log_id',
        'sale_location': 'sale_location',
        'confidence': 'confidence',
        'text_location': 'text_location'
    }

    def __init__(self, ticket_id=None, check_port=None, train_number=None, departure_station=None, destination_station=None, departure_station_en=None, destination_station_en=None, departure_time=None, seat_number=None, ticket_price=None, sale_method=None, seat_category=None, ticket_changing=None, id_number=None, name=None, log_id=None, sale_location=None, confidence=None, text_location=None):
        """TrainTicketResult

        The model defined in huaweicloud sdk

        :param ticket_id: 火车票左上角的车票ID。 
        :type ticket_id: str
        :param check_port: 检票口信息。 
        :type check_port: str
        :param train_number: 车次。 
        :type train_number: str
        :param departure_station: 始发站。 
        :type departure_station: str
        :param destination_station: 终点站。 
        :type destination_station: str
        :param departure_station_en: 始发站拼音。 
        :type departure_station_en: str
        :param destination_station_en: 终点站拼音。 
        :type destination_station_en: str
        :param departure_time: 开车时间。 
        :type departure_time: str
        :param seat_number: 座位号。 
        :type seat_number: str
        :param ticket_price: 票价。 
        :type ticket_price: str
        :param sale_method: 售票方式。 
        :type sale_method: str
        :param seat_category: 座位类别。 
        :type seat_category: str
        :param ticket_changing: 是否改签票, \&quot;Yes\&quot;表示改签票，\&quot;No\&quot;表示非改签票。 
        :type ticket_changing: str
        :param id_number: 车票持有人的身份证号。 
        :type id_number: str
        :param name: 车票持有人姓名。 
        :type name: str
        :param log_id: 车票最下方的序列号。 
        :type log_id: str
        :param sale_location: 车票售票地点。 
        :type sale_location: str
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。
        :type confidence: object
        :param text_location: 对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type text_location: object
        """
        
        

        self._ticket_id = None
        self._check_port = None
        self._train_number = None
        self._departure_station = None
        self._destination_station = None
        self._departure_station_en = None
        self._destination_station_en = None
        self._departure_time = None
        self._seat_number = None
        self._ticket_price = None
        self._sale_method = None
        self._seat_category = None
        self._ticket_changing = None
        self._id_number = None
        self._name = None
        self._log_id = None
        self._sale_location = None
        self._confidence = None
        self._text_location = None
        self.discriminator = None

        if ticket_id is not None:
            self.ticket_id = ticket_id
        if check_port is not None:
            self.check_port = check_port
        if train_number is not None:
            self.train_number = train_number
        if departure_station is not None:
            self.departure_station = departure_station
        if destination_station is not None:
            self.destination_station = destination_station
        if departure_station_en is not None:
            self.departure_station_en = departure_station_en
        if destination_station_en is not None:
            self.destination_station_en = destination_station_en
        if departure_time is not None:
            self.departure_time = departure_time
        if seat_number is not None:
            self.seat_number = seat_number
        if ticket_price is not None:
            self.ticket_price = ticket_price
        if sale_method is not None:
            self.sale_method = sale_method
        if seat_category is not None:
            self.seat_category = seat_category
        if ticket_changing is not None:
            self.ticket_changing = ticket_changing
        if id_number is not None:
            self.id_number = id_number
        if name is not None:
            self.name = name
        if log_id is not None:
            self.log_id = log_id
        if sale_location is not None:
            self.sale_location = sale_location
        if confidence is not None:
            self.confidence = confidence
        if text_location is not None:
            self.text_location = text_location

    @property
    def ticket_id(self):
        """Gets the ticket_id of this TrainTicketResult.

        火车票左上角的车票ID。 

        :return: The ticket_id of this TrainTicketResult.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        """Sets the ticket_id of this TrainTicketResult.

        火车票左上角的车票ID。 

        :param ticket_id: The ticket_id of this TrainTicketResult.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def check_port(self):
        """Gets the check_port of this TrainTicketResult.

        检票口信息。 

        :return: The check_port of this TrainTicketResult.
        :rtype: str
        """
        return self._check_port

    @check_port.setter
    def check_port(self, check_port):
        """Sets the check_port of this TrainTicketResult.

        检票口信息。 

        :param check_port: The check_port of this TrainTicketResult.
        :type check_port: str
        """
        self._check_port = check_port

    @property
    def train_number(self):
        """Gets the train_number of this TrainTicketResult.

        车次。 

        :return: The train_number of this TrainTicketResult.
        :rtype: str
        """
        return self._train_number

    @train_number.setter
    def train_number(self, train_number):
        """Sets the train_number of this TrainTicketResult.

        车次。 

        :param train_number: The train_number of this TrainTicketResult.
        :type train_number: str
        """
        self._train_number = train_number

    @property
    def departure_station(self):
        """Gets the departure_station of this TrainTicketResult.

        始发站。 

        :return: The departure_station of this TrainTicketResult.
        :rtype: str
        """
        return self._departure_station

    @departure_station.setter
    def departure_station(self, departure_station):
        """Sets the departure_station of this TrainTicketResult.

        始发站。 

        :param departure_station: The departure_station of this TrainTicketResult.
        :type departure_station: str
        """
        self._departure_station = departure_station

    @property
    def destination_station(self):
        """Gets the destination_station of this TrainTicketResult.

        终点站。 

        :return: The destination_station of this TrainTicketResult.
        :rtype: str
        """
        return self._destination_station

    @destination_station.setter
    def destination_station(self, destination_station):
        """Sets the destination_station of this TrainTicketResult.

        终点站。 

        :param destination_station: The destination_station of this TrainTicketResult.
        :type destination_station: str
        """
        self._destination_station = destination_station

    @property
    def departure_station_en(self):
        """Gets the departure_station_en of this TrainTicketResult.

        始发站拼音。 

        :return: The departure_station_en of this TrainTicketResult.
        :rtype: str
        """
        return self._departure_station_en

    @departure_station_en.setter
    def departure_station_en(self, departure_station_en):
        """Sets the departure_station_en of this TrainTicketResult.

        始发站拼音。 

        :param departure_station_en: The departure_station_en of this TrainTicketResult.
        :type departure_station_en: str
        """
        self._departure_station_en = departure_station_en

    @property
    def destination_station_en(self):
        """Gets the destination_station_en of this TrainTicketResult.

        终点站拼音。 

        :return: The destination_station_en of this TrainTicketResult.
        :rtype: str
        """
        return self._destination_station_en

    @destination_station_en.setter
    def destination_station_en(self, destination_station_en):
        """Sets the destination_station_en of this TrainTicketResult.

        终点站拼音。 

        :param destination_station_en: The destination_station_en of this TrainTicketResult.
        :type destination_station_en: str
        """
        self._destination_station_en = destination_station_en

    @property
    def departure_time(self):
        """Gets the departure_time of this TrainTicketResult.

        开车时间。 

        :return: The departure_time of this TrainTicketResult.
        :rtype: str
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        """Sets the departure_time of this TrainTicketResult.

        开车时间。 

        :param departure_time: The departure_time of this TrainTicketResult.
        :type departure_time: str
        """
        self._departure_time = departure_time

    @property
    def seat_number(self):
        """Gets the seat_number of this TrainTicketResult.

        座位号。 

        :return: The seat_number of this TrainTicketResult.
        :rtype: str
        """
        return self._seat_number

    @seat_number.setter
    def seat_number(self, seat_number):
        """Sets the seat_number of this TrainTicketResult.

        座位号。 

        :param seat_number: The seat_number of this TrainTicketResult.
        :type seat_number: str
        """
        self._seat_number = seat_number

    @property
    def ticket_price(self):
        """Gets the ticket_price of this TrainTicketResult.

        票价。 

        :return: The ticket_price of this TrainTicketResult.
        :rtype: str
        """
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, ticket_price):
        """Sets the ticket_price of this TrainTicketResult.

        票价。 

        :param ticket_price: The ticket_price of this TrainTicketResult.
        :type ticket_price: str
        """
        self._ticket_price = ticket_price

    @property
    def sale_method(self):
        """Gets the sale_method of this TrainTicketResult.

        售票方式。 

        :return: The sale_method of this TrainTicketResult.
        :rtype: str
        """
        return self._sale_method

    @sale_method.setter
    def sale_method(self, sale_method):
        """Sets the sale_method of this TrainTicketResult.

        售票方式。 

        :param sale_method: The sale_method of this TrainTicketResult.
        :type sale_method: str
        """
        self._sale_method = sale_method

    @property
    def seat_category(self):
        """Gets the seat_category of this TrainTicketResult.

        座位类别。 

        :return: The seat_category of this TrainTicketResult.
        :rtype: str
        """
        return self._seat_category

    @seat_category.setter
    def seat_category(self, seat_category):
        """Sets the seat_category of this TrainTicketResult.

        座位类别。 

        :param seat_category: The seat_category of this TrainTicketResult.
        :type seat_category: str
        """
        self._seat_category = seat_category

    @property
    def ticket_changing(self):
        """Gets the ticket_changing of this TrainTicketResult.

        是否改签票, \"Yes\"表示改签票，\"No\"表示非改签票。 

        :return: The ticket_changing of this TrainTicketResult.
        :rtype: str
        """
        return self._ticket_changing

    @ticket_changing.setter
    def ticket_changing(self, ticket_changing):
        """Sets the ticket_changing of this TrainTicketResult.

        是否改签票, \"Yes\"表示改签票，\"No\"表示非改签票。 

        :param ticket_changing: The ticket_changing of this TrainTicketResult.
        :type ticket_changing: str
        """
        self._ticket_changing = ticket_changing

    @property
    def id_number(self):
        """Gets the id_number of this TrainTicketResult.

        车票持有人的身份证号。 

        :return: The id_number of this TrainTicketResult.
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this TrainTicketResult.

        车票持有人的身份证号。 

        :param id_number: The id_number of this TrainTicketResult.
        :type id_number: str
        """
        self._id_number = id_number

    @property
    def name(self):
        """Gets the name of this TrainTicketResult.

        车票持有人姓名。 

        :return: The name of this TrainTicketResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrainTicketResult.

        车票持有人姓名。 

        :param name: The name of this TrainTicketResult.
        :type name: str
        """
        self._name = name

    @property
    def log_id(self):
        """Gets the log_id of this TrainTicketResult.

        车票最下方的序列号。 

        :return: The log_id of this TrainTicketResult.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this TrainTicketResult.

        车票最下方的序列号。 

        :param log_id: The log_id of this TrainTicketResult.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def sale_location(self):
        """Gets the sale_location of this TrainTicketResult.

        车票售票地点。 

        :return: The sale_location of this TrainTicketResult.
        :rtype: str
        """
        return self._sale_location

    @sale_location.setter
    def sale_location(self, sale_location):
        """Sets the sale_location of this TrainTicketResult.

        车票售票地点。 

        :param sale_location: The sale_location of this TrainTicketResult.
        :type sale_location: str
        """
        self._sale_location = sale_location

    @property
    def confidence(self):
        """Gets the confidence of this TrainTicketResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。

        :return: The confidence of this TrainTicketResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TrainTicketResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。

        :param confidence: The confidence of this TrainTicketResult.
        :type confidence: object
        """
        self._confidence = confidence

    @property
    def text_location(self):
        """Gets the text_location of this TrainTicketResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The text_location of this TrainTicketResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        """Sets the text_location of this TrainTicketResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param text_location: The text_location of this TrainTicketResult.
        :type text_location: object
        """
        self._text_location = text_location

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
        if not isinstance(other, TrainTicketResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
