# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VehicleCertificateResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_number': 'str',
        'issue_date': 'str',
        'manufacture_name': 'str',
        'vehicle_brand': 'str',
        'vehicle_name': 'str',
        'vehicle_model': 'str',
        'vin': 'str',
        'vehicle_color': 'str',
        'chassis_model': 'str',
        'chassis_id': 'str',
        'chassis_certificate_number': 'str',
        'engine_model': 'str',
        'engine_number': 'str',
        'fuel_type': 'str',
        'displacement': 'str',
        'power': 'str',
        'emission_standard': 'str',
        'fuel_consumption': 'str',
        'overall_dimension_length': 'str',
        'overall_dimension_width': 'str',
        'overall_dimension_height': 'str',
        'container_dimension_length': 'str',
        'container_dimension_width': 'str',
        'container_dimension_height': 'str',
        'spring_quantity': 'str',
        'tire_quantity': 'str',
        'tire_size': 'str',
        'front_wheel_track': 'str',
        'rear_wheel_track': 'str',
        'wheelbase': 'str',
        'axle_load': 'str',
        'axle_quantity': 'str',
        'steering_form': 'str',
        'total_weight': 'str',
        'equipment_weight': 'str',
        'maximum_laden_mass': 'str',
        'mass_utilization_coefficient': 'str',
        'traction_weight': 'str',
        'maximum_load_mass': 'str',
        'cab_passenger_capacity': 'str',
        'passenger_capacity': 'str',
        'max_design_speed': 'str',
        'manufacture_date': 'str',
        'confidence': 'object',
        'text_location': 'object'
    }

    attribute_map = {
        'certificate_number': 'certificate_number',
        'issue_date': 'issue_date',
        'manufacture_name': 'manufacture_name',
        'vehicle_brand': 'vehicle_brand',
        'vehicle_name': 'vehicle_name',
        'vehicle_model': 'vehicle_model',
        'vin': 'vin',
        'vehicle_color': 'vehicle_color',
        'chassis_model': 'chassis_model',
        'chassis_id': 'chassis_id',
        'chassis_certificate_number': 'chassis_certificate_number',
        'engine_model': 'engine_model',
        'engine_number': 'engine_number',
        'fuel_type': 'fuel_type',
        'displacement': 'displacement',
        'power': 'power',
        'emission_standard': 'emission_standard',
        'fuel_consumption': 'fuel_consumption',
        'overall_dimension_length': 'overall_dimension_length',
        'overall_dimension_width': 'overall_dimension_width',
        'overall_dimension_height': 'overall_dimension_height',
        'container_dimension_length': 'container_dimension_length',
        'container_dimension_width': 'container_dimension_width',
        'container_dimension_height': 'container_dimension_height',
        'spring_quantity': 'spring_quantity',
        'tire_quantity': 'tire_quantity',
        'tire_size': 'tire_size',
        'front_wheel_track': 'front_wheel_track',
        'rear_wheel_track': 'rear_wheel_track',
        'wheelbase': 'wheelbase',
        'axle_load': 'axle_load',
        'axle_quantity': 'axle_quantity',
        'steering_form': 'steering_form',
        'total_weight': 'total_weight',
        'equipment_weight': 'equipment_weight',
        'maximum_laden_mass': 'maximum_laden_mass',
        'mass_utilization_coefficient': 'mass_utilization_coefficient',
        'traction_weight': 'traction_weight',
        'maximum_load_mass': 'maximum_load_mass',
        'cab_passenger_capacity': 'cab_passenger_capacity',
        'passenger_capacity': 'passenger_capacity',
        'max_design_speed': 'max_design_speed',
        'manufacture_date': 'manufacture_date',
        'confidence': 'confidence',
        'text_location': 'text_location'
    }

    def __init__(self, certificate_number=None, issue_date=None, manufacture_name=None, vehicle_brand=None, vehicle_name=None, vehicle_model=None, vin=None, vehicle_color=None, chassis_model=None, chassis_id=None, chassis_certificate_number=None, engine_model=None, engine_number=None, fuel_type=None, displacement=None, power=None, emission_standard=None, fuel_consumption=None, overall_dimension_length=None, overall_dimension_width=None, overall_dimension_height=None, container_dimension_length=None, container_dimension_width=None, container_dimension_height=None, spring_quantity=None, tire_quantity=None, tire_size=None, front_wheel_track=None, rear_wheel_track=None, wheelbase=None, axle_load=None, axle_quantity=None, steering_form=None, total_weight=None, equipment_weight=None, maximum_laden_mass=None, mass_utilization_coefficient=None, traction_weight=None, maximum_load_mass=None, cab_passenger_capacity=None, passenger_capacity=None, max_design_speed=None, manufacture_date=None, confidence=None, text_location=None):
        r"""VehicleCertificateResult

        The model defined in huaweicloud sdk

        :param certificate_number: 合格证编号。 
        :type certificate_number: str
        :param issue_date: 发证日期。 
        :type issue_date: str
        :param manufacture_name: 车辆制造企业名称。 
        :type manufacture_name: str
        :param vehicle_brand: 车辆品牌。 
        :type vehicle_brand: str
        :param vehicle_name: 车辆名称。 
        :type vehicle_name: str
        :param vehicle_model: 车辆型号。 
        :type vehicle_model: str
        :param vin: 车架号。 
        :type vin: str
        :param vehicle_color: 车身颜色。 
        :type vehicle_color: str
        :param chassis_model: 底盘型号。 
        :type chassis_model: str
        :param chassis_id: 底盘ID。 
        :type chassis_id: str
        :param chassis_certificate_number: 底盘合格证编号。 
        :type chassis_certificate_number: str
        :param engine_model: 发动机型号。 
        :type engine_model: str
        :param engine_number: 发动机号。 
        :type engine_number: str
        :param fuel_type: 燃料种类。 
        :type fuel_type: str
        :param displacement: 排量。 
        :type displacement: str
        :param power: 功率。 
        :type power: str
        :param emission_standard: 排放标准。 
        :type emission_standard: str
        :param fuel_consumption: 油耗。 
        :type fuel_consumption: str
        :param overall_dimension_length: 外廓尺寸-长。 
        :type overall_dimension_length: str
        :param overall_dimension_width: 外廓尺寸-宽。 
        :type overall_dimension_width: str
        :param overall_dimension_height: 外廓尺寸-高。 
        :type overall_dimension_height: str
        :param container_dimension_length: 货厢内部尺寸-长。 
        :type container_dimension_length: str
        :param container_dimension_width: 货厢内部尺寸-宽。 
        :type container_dimension_width: str
        :param container_dimension_height: 货厢内部尺寸-高。 
        :type container_dimension_height: str
        :param spring_quantity: 钢板弹簧片数。 
        :type spring_quantity: str
        :param tire_quantity: 轮胎数。 
        :type tire_quantity: str
        :param tire_size: 轮胎规格。 
        :type tire_size: str
        :param front_wheel_track: 轮距-前。 
        :type front_wheel_track: str
        :param rear_wheel_track: 轮距-后。 
        :type rear_wheel_track: str
        :param wheelbase: 轴距。 
        :type wheelbase: str
        :param axle_load: 轴荷。 
        :type axle_load: str
        :param axle_quantity: 轴数。 
        :type axle_quantity: str
        :param steering_form: 转向形式。 
        :type steering_form: str
        :param total_weight: 总质量。 
        :type total_weight: str
        :param equipment_weight: 整备质量。 
        :type equipment_weight: str
        :param maximum_laden_mass: 额定载质量。 
        :type maximum_laden_mass: str
        :param mass_utilization_coefficient: 载质量利用系数。 
        :type mass_utilization_coefficient: str
        :param traction_weight: 准牵引总质量。 
        :type traction_weight: str
        :param maximum_load_mass: 半挂车鞍座最大允许总质量。 
        :type maximum_load_mass: str
        :param cab_passenger_capacity: 驾驶室准乘人数。 
        :type cab_passenger_capacity: str
        :param passenger_capacity: 额定载客。 
        :type passenger_capacity: str
        :param max_design_speed: 最高设计车速。 
        :type max_design_speed: str
        :param manufacture_date: 车辆制造日期。 
        :type manufacture_date: str
        :param confidence: 字段的置信度，取值范围0~1。 置信度越大，本次识别的字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于字段的准确率。 
        :type confidence: object
        :param text_location: 对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type text_location: object
        """
        
        

        self._certificate_number = None
        self._issue_date = None
        self._manufacture_name = None
        self._vehicle_brand = None
        self._vehicle_name = None
        self._vehicle_model = None
        self._vin = None
        self._vehicle_color = None
        self._chassis_model = None
        self._chassis_id = None
        self._chassis_certificate_number = None
        self._engine_model = None
        self._engine_number = None
        self._fuel_type = None
        self._displacement = None
        self._power = None
        self._emission_standard = None
        self._fuel_consumption = None
        self._overall_dimension_length = None
        self._overall_dimension_width = None
        self._overall_dimension_height = None
        self._container_dimension_length = None
        self._container_dimension_width = None
        self._container_dimension_height = None
        self._spring_quantity = None
        self._tire_quantity = None
        self._tire_size = None
        self._front_wheel_track = None
        self._rear_wheel_track = None
        self._wheelbase = None
        self._axle_load = None
        self._axle_quantity = None
        self._steering_form = None
        self._total_weight = None
        self._equipment_weight = None
        self._maximum_laden_mass = None
        self._mass_utilization_coefficient = None
        self._traction_weight = None
        self._maximum_load_mass = None
        self._cab_passenger_capacity = None
        self._passenger_capacity = None
        self._max_design_speed = None
        self._manufacture_date = None
        self._confidence = None
        self._text_location = None
        self.discriminator = None

        if certificate_number is not None:
            self.certificate_number = certificate_number
        if issue_date is not None:
            self.issue_date = issue_date
        if manufacture_name is not None:
            self.manufacture_name = manufacture_name
        if vehicle_brand is not None:
            self.vehicle_brand = vehicle_brand
        if vehicle_name is not None:
            self.vehicle_name = vehicle_name
        if vehicle_model is not None:
            self.vehicle_model = vehicle_model
        if vin is not None:
            self.vin = vin
        if vehicle_color is not None:
            self.vehicle_color = vehicle_color
        if chassis_model is not None:
            self.chassis_model = chassis_model
        if chassis_id is not None:
            self.chassis_id = chassis_id
        if chassis_certificate_number is not None:
            self.chassis_certificate_number = chassis_certificate_number
        if engine_model is not None:
            self.engine_model = engine_model
        if engine_number is not None:
            self.engine_number = engine_number
        if fuel_type is not None:
            self.fuel_type = fuel_type
        if displacement is not None:
            self.displacement = displacement
        if power is not None:
            self.power = power
        if emission_standard is not None:
            self.emission_standard = emission_standard
        if fuel_consumption is not None:
            self.fuel_consumption = fuel_consumption
        if overall_dimension_length is not None:
            self.overall_dimension_length = overall_dimension_length
        if overall_dimension_width is not None:
            self.overall_dimension_width = overall_dimension_width
        if overall_dimension_height is not None:
            self.overall_dimension_height = overall_dimension_height
        if container_dimension_length is not None:
            self.container_dimension_length = container_dimension_length
        if container_dimension_width is not None:
            self.container_dimension_width = container_dimension_width
        if container_dimension_height is not None:
            self.container_dimension_height = container_dimension_height
        if spring_quantity is not None:
            self.spring_quantity = spring_quantity
        if tire_quantity is not None:
            self.tire_quantity = tire_quantity
        if tire_size is not None:
            self.tire_size = tire_size
        if front_wheel_track is not None:
            self.front_wheel_track = front_wheel_track
        if rear_wheel_track is not None:
            self.rear_wheel_track = rear_wheel_track
        if wheelbase is not None:
            self.wheelbase = wheelbase
        if axle_load is not None:
            self.axle_load = axle_load
        if axle_quantity is not None:
            self.axle_quantity = axle_quantity
        if steering_form is not None:
            self.steering_form = steering_form
        if total_weight is not None:
            self.total_weight = total_weight
        if equipment_weight is not None:
            self.equipment_weight = equipment_weight
        if maximum_laden_mass is not None:
            self.maximum_laden_mass = maximum_laden_mass
        if mass_utilization_coefficient is not None:
            self.mass_utilization_coefficient = mass_utilization_coefficient
        if traction_weight is not None:
            self.traction_weight = traction_weight
        if maximum_load_mass is not None:
            self.maximum_load_mass = maximum_load_mass
        if cab_passenger_capacity is not None:
            self.cab_passenger_capacity = cab_passenger_capacity
        if passenger_capacity is not None:
            self.passenger_capacity = passenger_capacity
        if max_design_speed is not None:
            self.max_design_speed = max_design_speed
        if manufacture_date is not None:
            self.manufacture_date = manufacture_date
        if confidence is not None:
            self.confidence = confidence
        if text_location is not None:
            self.text_location = text_location

    @property
    def certificate_number(self):
        r"""Gets the certificate_number of this VehicleCertificateResult.

        合格证编号。 

        :return: The certificate_number of this VehicleCertificateResult.
        :rtype: str
        """
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, certificate_number):
        r"""Sets the certificate_number of this VehicleCertificateResult.

        合格证编号。 

        :param certificate_number: The certificate_number of this VehicleCertificateResult.
        :type certificate_number: str
        """
        self._certificate_number = certificate_number

    @property
    def issue_date(self):
        r"""Gets the issue_date of this VehicleCertificateResult.

        发证日期。 

        :return: The issue_date of this VehicleCertificateResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this VehicleCertificateResult.

        发证日期。 

        :param issue_date: The issue_date of this VehicleCertificateResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def manufacture_name(self):
        r"""Gets the manufacture_name of this VehicleCertificateResult.

        车辆制造企业名称。 

        :return: The manufacture_name of this VehicleCertificateResult.
        :rtype: str
        """
        return self._manufacture_name

    @manufacture_name.setter
    def manufacture_name(self, manufacture_name):
        r"""Sets the manufacture_name of this VehicleCertificateResult.

        车辆制造企业名称。 

        :param manufacture_name: The manufacture_name of this VehicleCertificateResult.
        :type manufacture_name: str
        """
        self._manufacture_name = manufacture_name

    @property
    def vehicle_brand(self):
        r"""Gets the vehicle_brand of this VehicleCertificateResult.

        车辆品牌。 

        :return: The vehicle_brand of this VehicleCertificateResult.
        :rtype: str
        """
        return self._vehicle_brand

    @vehicle_brand.setter
    def vehicle_brand(self, vehicle_brand):
        r"""Sets the vehicle_brand of this VehicleCertificateResult.

        车辆品牌。 

        :param vehicle_brand: The vehicle_brand of this VehicleCertificateResult.
        :type vehicle_brand: str
        """
        self._vehicle_brand = vehicle_brand

    @property
    def vehicle_name(self):
        r"""Gets the vehicle_name of this VehicleCertificateResult.

        车辆名称。 

        :return: The vehicle_name of this VehicleCertificateResult.
        :rtype: str
        """
        return self._vehicle_name

    @vehicle_name.setter
    def vehicle_name(self, vehicle_name):
        r"""Sets the vehicle_name of this VehicleCertificateResult.

        车辆名称。 

        :param vehicle_name: The vehicle_name of this VehicleCertificateResult.
        :type vehicle_name: str
        """
        self._vehicle_name = vehicle_name

    @property
    def vehicle_model(self):
        r"""Gets the vehicle_model of this VehicleCertificateResult.

        车辆型号。 

        :return: The vehicle_model of this VehicleCertificateResult.
        :rtype: str
        """
        return self._vehicle_model

    @vehicle_model.setter
    def vehicle_model(self, vehicle_model):
        r"""Sets the vehicle_model of this VehicleCertificateResult.

        车辆型号。 

        :param vehicle_model: The vehicle_model of this VehicleCertificateResult.
        :type vehicle_model: str
        """
        self._vehicle_model = vehicle_model

    @property
    def vin(self):
        r"""Gets the vin of this VehicleCertificateResult.

        车架号。 

        :return: The vin of this VehicleCertificateResult.
        :rtype: str
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        r"""Sets the vin of this VehicleCertificateResult.

        车架号。 

        :param vin: The vin of this VehicleCertificateResult.
        :type vin: str
        """
        self._vin = vin

    @property
    def vehicle_color(self):
        r"""Gets the vehicle_color of this VehicleCertificateResult.

        车身颜色。 

        :return: The vehicle_color of this VehicleCertificateResult.
        :rtype: str
        """
        return self._vehicle_color

    @vehicle_color.setter
    def vehicle_color(self, vehicle_color):
        r"""Sets the vehicle_color of this VehicleCertificateResult.

        车身颜色。 

        :param vehicle_color: The vehicle_color of this VehicleCertificateResult.
        :type vehicle_color: str
        """
        self._vehicle_color = vehicle_color

    @property
    def chassis_model(self):
        r"""Gets the chassis_model of this VehicleCertificateResult.

        底盘型号。 

        :return: The chassis_model of this VehicleCertificateResult.
        :rtype: str
        """
        return self._chassis_model

    @chassis_model.setter
    def chassis_model(self, chassis_model):
        r"""Sets the chassis_model of this VehicleCertificateResult.

        底盘型号。 

        :param chassis_model: The chassis_model of this VehicleCertificateResult.
        :type chassis_model: str
        """
        self._chassis_model = chassis_model

    @property
    def chassis_id(self):
        r"""Gets the chassis_id of this VehicleCertificateResult.

        底盘ID。 

        :return: The chassis_id of this VehicleCertificateResult.
        :rtype: str
        """
        return self._chassis_id

    @chassis_id.setter
    def chassis_id(self, chassis_id):
        r"""Sets the chassis_id of this VehicleCertificateResult.

        底盘ID。 

        :param chassis_id: The chassis_id of this VehicleCertificateResult.
        :type chassis_id: str
        """
        self._chassis_id = chassis_id

    @property
    def chassis_certificate_number(self):
        r"""Gets the chassis_certificate_number of this VehicleCertificateResult.

        底盘合格证编号。 

        :return: The chassis_certificate_number of this VehicleCertificateResult.
        :rtype: str
        """
        return self._chassis_certificate_number

    @chassis_certificate_number.setter
    def chassis_certificate_number(self, chassis_certificate_number):
        r"""Sets the chassis_certificate_number of this VehicleCertificateResult.

        底盘合格证编号。 

        :param chassis_certificate_number: The chassis_certificate_number of this VehicleCertificateResult.
        :type chassis_certificate_number: str
        """
        self._chassis_certificate_number = chassis_certificate_number

    @property
    def engine_model(self):
        r"""Gets the engine_model of this VehicleCertificateResult.

        发动机型号。 

        :return: The engine_model of this VehicleCertificateResult.
        :rtype: str
        """
        return self._engine_model

    @engine_model.setter
    def engine_model(self, engine_model):
        r"""Sets the engine_model of this VehicleCertificateResult.

        发动机型号。 

        :param engine_model: The engine_model of this VehicleCertificateResult.
        :type engine_model: str
        """
        self._engine_model = engine_model

    @property
    def engine_number(self):
        r"""Gets the engine_number of this VehicleCertificateResult.

        发动机号。 

        :return: The engine_number of this VehicleCertificateResult.
        :rtype: str
        """
        return self._engine_number

    @engine_number.setter
    def engine_number(self, engine_number):
        r"""Sets the engine_number of this VehicleCertificateResult.

        发动机号。 

        :param engine_number: The engine_number of this VehicleCertificateResult.
        :type engine_number: str
        """
        self._engine_number = engine_number

    @property
    def fuel_type(self):
        r"""Gets the fuel_type of this VehicleCertificateResult.

        燃料种类。 

        :return: The fuel_type of this VehicleCertificateResult.
        :rtype: str
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        r"""Sets the fuel_type of this VehicleCertificateResult.

        燃料种类。 

        :param fuel_type: The fuel_type of this VehicleCertificateResult.
        :type fuel_type: str
        """
        self._fuel_type = fuel_type

    @property
    def displacement(self):
        r"""Gets the displacement of this VehicleCertificateResult.

        排量。 

        :return: The displacement of this VehicleCertificateResult.
        :rtype: str
        """
        return self._displacement

    @displacement.setter
    def displacement(self, displacement):
        r"""Sets the displacement of this VehicleCertificateResult.

        排量。 

        :param displacement: The displacement of this VehicleCertificateResult.
        :type displacement: str
        """
        self._displacement = displacement

    @property
    def power(self):
        r"""Gets the power of this VehicleCertificateResult.

        功率。 

        :return: The power of this VehicleCertificateResult.
        :rtype: str
        """
        return self._power

    @power.setter
    def power(self, power):
        r"""Sets the power of this VehicleCertificateResult.

        功率。 

        :param power: The power of this VehicleCertificateResult.
        :type power: str
        """
        self._power = power

    @property
    def emission_standard(self):
        r"""Gets the emission_standard of this VehicleCertificateResult.

        排放标准。 

        :return: The emission_standard of this VehicleCertificateResult.
        :rtype: str
        """
        return self._emission_standard

    @emission_standard.setter
    def emission_standard(self, emission_standard):
        r"""Sets the emission_standard of this VehicleCertificateResult.

        排放标准。 

        :param emission_standard: The emission_standard of this VehicleCertificateResult.
        :type emission_standard: str
        """
        self._emission_standard = emission_standard

    @property
    def fuel_consumption(self):
        r"""Gets the fuel_consumption of this VehicleCertificateResult.

        油耗。 

        :return: The fuel_consumption of this VehicleCertificateResult.
        :rtype: str
        """
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, fuel_consumption):
        r"""Sets the fuel_consumption of this VehicleCertificateResult.

        油耗。 

        :param fuel_consumption: The fuel_consumption of this VehicleCertificateResult.
        :type fuel_consumption: str
        """
        self._fuel_consumption = fuel_consumption

    @property
    def overall_dimension_length(self):
        r"""Gets the overall_dimension_length of this VehicleCertificateResult.

        外廓尺寸-长。 

        :return: The overall_dimension_length of this VehicleCertificateResult.
        :rtype: str
        """
        return self._overall_dimension_length

    @overall_dimension_length.setter
    def overall_dimension_length(self, overall_dimension_length):
        r"""Sets the overall_dimension_length of this VehicleCertificateResult.

        外廓尺寸-长。 

        :param overall_dimension_length: The overall_dimension_length of this VehicleCertificateResult.
        :type overall_dimension_length: str
        """
        self._overall_dimension_length = overall_dimension_length

    @property
    def overall_dimension_width(self):
        r"""Gets the overall_dimension_width of this VehicleCertificateResult.

        外廓尺寸-宽。 

        :return: The overall_dimension_width of this VehicleCertificateResult.
        :rtype: str
        """
        return self._overall_dimension_width

    @overall_dimension_width.setter
    def overall_dimension_width(self, overall_dimension_width):
        r"""Sets the overall_dimension_width of this VehicleCertificateResult.

        外廓尺寸-宽。 

        :param overall_dimension_width: The overall_dimension_width of this VehicleCertificateResult.
        :type overall_dimension_width: str
        """
        self._overall_dimension_width = overall_dimension_width

    @property
    def overall_dimension_height(self):
        r"""Gets the overall_dimension_height of this VehicleCertificateResult.

        外廓尺寸-高。 

        :return: The overall_dimension_height of this VehicleCertificateResult.
        :rtype: str
        """
        return self._overall_dimension_height

    @overall_dimension_height.setter
    def overall_dimension_height(self, overall_dimension_height):
        r"""Sets the overall_dimension_height of this VehicleCertificateResult.

        外廓尺寸-高。 

        :param overall_dimension_height: The overall_dimension_height of this VehicleCertificateResult.
        :type overall_dimension_height: str
        """
        self._overall_dimension_height = overall_dimension_height

    @property
    def container_dimension_length(self):
        r"""Gets the container_dimension_length of this VehicleCertificateResult.

        货厢内部尺寸-长。 

        :return: The container_dimension_length of this VehicleCertificateResult.
        :rtype: str
        """
        return self._container_dimension_length

    @container_dimension_length.setter
    def container_dimension_length(self, container_dimension_length):
        r"""Sets the container_dimension_length of this VehicleCertificateResult.

        货厢内部尺寸-长。 

        :param container_dimension_length: The container_dimension_length of this VehicleCertificateResult.
        :type container_dimension_length: str
        """
        self._container_dimension_length = container_dimension_length

    @property
    def container_dimension_width(self):
        r"""Gets the container_dimension_width of this VehicleCertificateResult.

        货厢内部尺寸-宽。 

        :return: The container_dimension_width of this VehicleCertificateResult.
        :rtype: str
        """
        return self._container_dimension_width

    @container_dimension_width.setter
    def container_dimension_width(self, container_dimension_width):
        r"""Sets the container_dimension_width of this VehicleCertificateResult.

        货厢内部尺寸-宽。 

        :param container_dimension_width: The container_dimension_width of this VehicleCertificateResult.
        :type container_dimension_width: str
        """
        self._container_dimension_width = container_dimension_width

    @property
    def container_dimension_height(self):
        r"""Gets the container_dimension_height of this VehicleCertificateResult.

        货厢内部尺寸-高。 

        :return: The container_dimension_height of this VehicleCertificateResult.
        :rtype: str
        """
        return self._container_dimension_height

    @container_dimension_height.setter
    def container_dimension_height(self, container_dimension_height):
        r"""Sets the container_dimension_height of this VehicleCertificateResult.

        货厢内部尺寸-高。 

        :param container_dimension_height: The container_dimension_height of this VehicleCertificateResult.
        :type container_dimension_height: str
        """
        self._container_dimension_height = container_dimension_height

    @property
    def spring_quantity(self):
        r"""Gets the spring_quantity of this VehicleCertificateResult.

        钢板弹簧片数。 

        :return: The spring_quantity of this VehicleCertificateResult.
        :rtype: str
        """
        return self._spring_quantity

    @spring_quantity.setter
    def spring_quantity(self, spring_quantity):
        r"""Sets the spring_quantity of this VehicleCertificateResult.

        钢板弹簧片数。 

        :param spring_quantity: The spring_quantity of this VehicleCertificateResult.
        :type spring_quantity: str
        """
        self._spring_quantity = spring_quantity

    @property
    def tire_quantity(self):
        r"""Gets the tire_quantity of this VehicleCertificateResult.

        轮胎数。 

        :return: The tire_quantity of this VehicleCertificateResult.
        :rtype: str
        """
        return self._tire_quantity

    @tire_quantity.setter
    def tire_quantity(self, tire_quantity):
        r"""Sets the tire_quantity of this VehicleCertificateResult.

        轮胎数。 

        :param tire_quantity: The tire_quantity of this VehicleCertificateResult.
        :type tire_quantity: str
        """
        self._tire_quantity = tire_quantity

    @property
    def tire_size(self):
        r"""Gets the tire_size of this VehicleCertificateResult.

        轮胎规格。 

        :return: The tire_size of this VehicleCertificateResult.
        :rtype: str
        """
        return self._tire_size

    @tire_size.setter
    def tire_size(self, tire_size):
        r"""Sets the tire_size of this VehicleCertificateResult.

        轮胎规格。 

        :param tire_size: The tire_size of this VehicleCertificateResult.
        :type tire_size: str
        """
        self._tire_size = tire_size

    @property
    def front_wheel_track(self):
        r"""Gets the front_wheel_track of this VehicleCertificateResult.

        轮距-前。 

        :return: The front_wheel_track of this VehicleCertificateResult.
        :rtype: str
        """
        return self._front_wheel_track

    @front_wheel_track.setter
    def front_wheel_track(self, front_wheel_track):
        r"""Sets the front_wheel_track of this VehicleCertificateResult.

        轮距-前。 

        :param front_wheel_track: The front_wheel_track of this VehicleCertificateResult.
        :type front_wheel_track: str
        """
        self._front_wheel_track = front_wheel_track

    @property
    def rear_wheel_track(self):
        r"""Gets the rear_wheel_track of this VehicleCertificateResult.

        轮距-后。 

        :return: The rear_wheel_track of this VehicleCertificateResult.
        :rtype: str
        """
        return self._rear_wheel_track

    @rear_wheel_track.setter
    def rear_wheel_track(self, rear_wheel_track):
        r"""Sets the rear_wheel_track of this VehicleCertificateResult.

        轮距-后。 

        :param rear_wheel_track: The rear_wheel_track of this VehicleCertificateResult.
        :type rear_wheel_track: str
        """
        self._rear_wheel_track = rear_wheel_track

    @property
    def wheelbase(self):
        r"""Gets the wheelbase of this VehicleCertificateResult.

        轴距。 

        :return: The wheelbase of this VehicleCertificateResult.
        :rtype: str
        """
        return self._wheelbase

    @wheelbase.setter
    def wheelbase(self, wheelbase):
        r"""Sets the wheelbase of this VehicleCertificateResult.

        轴距。 

        :param wheelbase: The wheelbase of this VehicleCertificateResult.
        :type wheelbase: str
        """
        self._wheelbase = wheelbase

    @property
    def axle_load(self):
        r"""Gets the axle_load of this VehicleCertificateResult.

        轴荷。 

        :return: The axle_load of this VehicleCertificateResult.
        :rtype: str
        """
        return self._axle_load

    @axle_load.setter
    def axle_load(self, axle_load):
        r"""Sets the axle_load of this VehicleCertificateResult.

        轴荷。 

        :param axle_load: The axle_load of this VehicleCertificateResult.
        :type axle_load: str
        """
        self._axle_load = axle_load

    @property
    def axle_quantity(self):
        r"""Gets the axle_quantity of this VehicleCertificateResult.

        轴数。 

        :return: The axle_quantity of this VehicleCertificateResult.
        :rtype: str
        """
        return self._axle_quantity

    @axle_quantity.setter
    def axle_quantity(self, axle_quantity):
        r"""Sets the axle_quantity of this VehicleCertificateResult.

        轴数。 

        :param axle_quantity: The axle_quantity of this VehicleCertificateResult.
        :type axle_quantity: str
        """
        self._axle_quantity = axle_quantity

    @property
    def steering_form(self):
        r"""Gets the steering_form of this VehicleCertificateResult.

        转向形式。 

        :return: The steering_form of this VehicleCertificateResult.
        :rtype: str
        """
        return self._steering_form

    @steering_form.setter
    def steering_form(self, steering_form):
        r"""Sets the steering_form of this VehicleCertificateResult.

        转向形式。 

        :param steering_form: The steering_form of this VehicleCertificateResult.
        :type steering_form: str
        """
        self._steering_form = steering_form

    @property
    def total_weight(self):
        r"""Gets the total_weight of this VehicleCertificateResult.

        总质量。 

        :return: The total_weight of this VehicleCertificateResult.
        :rtype: str
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, total_weight):
        r"""Sets the total_weight of this VehicleCertificateResult.

        总质量。 

        :param total_weight: The total_weight of this VehicleCertificateResult.
        :type total_weight: str
        """
        self._total_weight = total_weight

    @property
    def equipment_weight(self):
        r"""Gets the equipment_weight of this VehicleCertificateResult.

        整备质量。 

        :return: The equipment_weight of this VehicleCertificateResult.
        :rtype: str
        """
        return self._equipment_weight

    @equipment_weight.setter
    def equipment_weight(self, equipment_weight):
        r"""Sets the equipment_weight of this VehicleCertificateResult.

        整备质量。 

        :param equipment_weight: The equipment_weight of this VehicleCertificateResult.
        :type equipment_weight: str
        """
        self._equipment_weight = equipment_weight

    @property
    def maximum_laden_mass(self):
        r"""Gets the maximum_laden_mass of this VehicleCertificateResult.

        额定载质量。 

        :return: The maximum_laden_mass of this VehicleCertificateResult.
        :rtype: str
        """
        return self._maximum_laden_mass

    @maximum_laden_mass.setter
    def maximum_laden_mass(self, maximum_laden_mass):
        r"""Sets the maximum_laden_mass of this VehicleCertificateResult.

        额定载质量。 

        :param maximum_laden_mass: The maximum_laden_mass of this VehicleCertificateResult.
        :type maximum_laden_mass: str
        """
        self._maximum_laden_mass = maximum_laden_mass

    @property
    def mass_utilization_coefficient(self):
        r"""Gets the mass_utilization_coefficient of this VehicleCertificateResult.

        载质量利用系数。 

        :return: The mass_utilization_coefficient of this VehicleCertificateResult.
        :rtype: str
        """
        return self._mass_utilization_coefficient

    @mass_utilization_coefficient.setter
    def mass_utilization_coefficient(self, mass_utilization_coefficient):
        r"""Sets the mass_utilization_coefficient of this VehicleCertificateResult.

        载质量利用系数。 

        :param mass_utilization_coefficient: The mass_utilization_coefficient of this VehicleCertificateResult.
        :type mass_utilization_coefficient: str
        """
        self._mass_utilization_coefficient = mass_utilization_coefficient

    @property
    def traction_weight(self):
        r"""Gets the traction_weight of this VehicleCertificateResult.

        准牵引总质量。 

        :return: The traction_weight of this VehicleCertificateResult.
        :rtype: str
        """
        return self._traction_weight

    @traction_weight.setter
    def traction_weight(self, traction_weight):
        r"""Sets the traction_weight of this VehicleCertificateResult.

        准牵引总质量。 

        :param traction_weight: The traction_weight of this VehicleCertificateResult.
        :type traction_weight: str
        """
        self._traction_weight = traction_weight

    @property
    def maximum_load_mass(self):
        r"""Gets the maximum_load_mass of this VehicleCertificateResult.

        半挂车鞍座最大允许总质量。 

        :return: The maximum_load_mass of this VehicleCertificateResult.
        :rtype: str
        """
        return self._maximum_load_mass

    @maximum_load_mass.setter
    def maximum_load_mass(self, maximum_load_mass):
        r"""Sets the maximum_load_mass of this VehicleCertificateResult.

        半挂车鞍座最大允许总质量。 

        :param maximum_load_mass: The maximum_load_mass of this VehicleCertificateResult.
        :type maximum_load_mass: str
        """
        self._maximum_load_mass = maximum_load_mass

    @property
    def cab_passenger_capacity(self):
        r"""Gets the cab_passenger_capacity of this VehicleCertificateResult.

        驾驶室准乘人数。 

        :return: The cab_passenger_capacity of this VehicleCertificateResult.
        :rtype: str
        """
        return self._cab_passenger_capacity

    @cab_passenger_capacity.setter
    def cab_passenger_capacity(self, cab_passenger_capacity):
        r"""Sets the cab_passenger_capacity of this VehicleCertificateResult.

        驾驶室准乘人数。 

        :param cab_passenger_capacity: The cab_passenger_capacity of this VehicleCertificateResult.
        :type cab_passenger_capacity: str
        """
        self._cab_passenger_capacity = cab_passenger_capacity

    @property
    def passenger_capacity(self):
        r"""Gets the passenger_capacity of this VehicleCertificateResult.

        额定载客。 

        :return: The passenger_capacity of this VehicleCertificateResult.
        :rtype: str
        """
        return self._passenger_capacity

    @passenger_capacity.setter
    def passenger_capacity(self, passenger_capacity):
        r"""Sets the passenger_capacity of this VehicleCertificateResult.

        额定载客。 

        :param passenger_capacity: The passenger_capacity of this VehicleCertificateResult.
        :type passenger_capacity: str
        """
        self._passenger_capacity = passenger_capacity

    @property
    def max_design_speed(self):
        r"""Gets the max_design_speed of this VehicleCertificateResult.

        最高设计车速。 

        :return: The max_design_speed of this VehicleCertificateResult.
        :rtype: str
        """
        return self._max_design_speed

    @max_design_speed.setter
    def max_design_speed(self, max_design_speed):
        r"""Sets the max_design_speed of this VehicleCertificateResult.

        最高设计车速。 

        :param max_design_speed: The max_design_speed of this VehicleCertificateResult.
        :type max_design_speed: str
        """
        self._max_design_speed = max_design_speed

    @property
    def manufacture_date(self):
        r"""Gets the manufacture_date of this VehicleCertificateResult.

        车辆制造日期。 

        :return: The manufacture_date of this VehicleCertificateResult.
        :rtype: str
        """
        return self._manufacture_date

    @manufacture_date.setter
    def manufacture_date(self, manufacture_date):
        r"""Sets the manufacture_date of this VehicleCertificateResult.

        车辆制造日期。 

        :param manufacture_date: The manufacture_date of this VehicleCertificateResult.
        :type manufacture_date: str
        """
        self._manufacture_date = manufacture_date

    @property
    def confidence(self):
        r"""Gets the confidence of this VehicleCertificateResult.

        字段的置信度，取值范围0~1。 置信度越大，本次识别的字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于字段的准确率。 

        :return: The confidence of this VehicleCertificateResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this VehicleCertificateResult.

        字段的置信度，取值范围0~1。 置信度越大，本次识别的字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于字段的准确率。 

        :param confidence: The confidence of this VehicleCertificateResult.
        :type confidence: object
        """
        self._confidence = confidence

    @property
    def text_location(self):
        r"""Gets the text_location of this VehicleCertificateResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The text_location of this VehicleCertificateResult.
        :rtype: object
        """
        return self._text_location

    @text_location.setter
    def text_location(self, text_location):
        r"""Sets the text_location of this VehicleCertificateResult.

        对应所有在原图上识别到的字段位置信息，包含所有文字区域四个顶点的二维坐标（x,y）。采用图像坐标系，坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param text_location: The text_location of this VehicleCertificateResult.
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
        if not isinstance(other, VehicleCertificateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
